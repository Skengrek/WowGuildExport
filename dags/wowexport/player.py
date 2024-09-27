from datetime import datetime
from logging import getLogger
from sqlalchemy.orm import Session
from sqlalchemy import select, desc
from sqlalchemy import Table, MetaData
from .utils import call, get_database_engine
from airflow.decorators import task, task_group
logger = getLogger(__name__)


@task_group
def player_task_group(roster: list):
    a = roster_response_to_player_list(roster)
    b = insert_new_char_to_database(a)
    new_char_equipment = get_char_equipment_from_api(a)
    b >> new_char_equipment

    insert_equipment_if_updated(new_char_equipment)

@task
def roster_response_to_player_list(roster_response: dict)-> list:
    players = []
    for char in roster_response["members"]:
        players.append({
            "id": char['character']['id'],
            "name": char['character']['name'],
            "server": char['character']['realm']['slug'],
        })
    
    get_all_known_characters_from_db()
    return players


@task
def get_char_equipment_from_api(user_list: list)->list:
    player_equipment = []
    for user in user_list:
        url = f"https://eu.api.blizzard.com/profile/wow/character/{user['server']}/{user['name'].lower()}/equipment"
        hearders = {
            "Battlenet-Namespace": "profile-eu"
        }
        try: 
            resp = call(url, hearders)
            player_equipment.append(resp)
        except Exception:
            logger.info(f"{user['name']} does not exist anymore")
    return player_equipment

@task
def insert_equipment_if_updated(new_char_equipment):

    engine = get_database_engine()
    metadata = MetaData(bind=engine)
    character_equipment_table = Table('equipments', metadata, autoload_with=engine)

    for _char in new_char_equipment:
        with engine.connect() as conn:
            new_equipment = {
                "character_id": _char["character"]["id"],
                "datetime": datetime.now(),
            }
            sum_ilevel = 0
            nb_items = 0
            item_list = []
            for eq in _char["equipped_items"]:
                if eq['slot']['type'].lower() not in ["shirt", "tabard"]:
                    nb_items += 1
                    sum_ilevel += eq['level']['value']
                    item_list.append(eq['slot']['type'].lower())
                    new_equipment[f"{eq['slot']['type'].lower()}_item_id"] = eq['item']['id']
                    new_equipment[f"{eq['slot']['type'].lower()}_item_quality"] = eq['quality']['type']
                    new_equipment[f"{eq['slot']['type'].lower()}_item_level"] = eq['level']['value']
            
            mean_ilevel = sum_ilevel/nb_items if nb_items > 0 else 0
            character_id = _char["character"]["id"]
            new_equipment["mean_item_level"] = mean_ilevel
            stmt = (
                select(character_equipment_table)
                .where(character_equipment_table.c.character_id == str(character_id))
                .order_by(desc(character_equipment_table.c.datetime))
                .limit(1)
            )
            result = conn.execute(stmt).mappings().fetchone()
            if not result:
                conn.execute(character_equipment_table.insert(new_equipment))
            else:
                update = False
                for item in item_list:
                    if f"{item}_item_level" not in result:
                        update = True
                        break
                    else:
                        if new_equipment[f"{item}_item_level"] != result[f"{item}_item_level"]:
                            update = True
                            break
                if update:
                    logger.info(f"update equipment of {_char["character"]["name"]}")
                    conn.execute(character_equipment_table.insert(new_equipment))

def extract_data_from_request(request: dict)-> dict:
    _dict =  {
        "player": request["character"]["name"],
    }

    for el in request["equipped_items"]:
        _dict[el["slot"]["type"]+"_ilevel"] = el["level"]["value"]
        _dict[el["slot"]["type"]+"_id"] = el["item"]["id"]
    
    return _dict

def get_all_known_characters_from_db() -> list:
    engine = get_database_engine()
    metadata = MetaData(bind=engine)
    character_table = Table('characters', metadata, autoload_with=engine)
    with Session(bind=engine) as session:
        ids = session.query(character_table).with_entities(character_table.columns.id).all()
        return [_id[0] for _id in ids]


@task
def insert_new_char_to_database(character_list):
    already_known_char_id = get_all_known_characters_from_db()
    logger.info(type(already_known_char_id[0]))
    character_to_add = []
    for p in character_list:
        if str(p["id"]) not in already_known_char_id:
            character_to_add.append({"name": p["name"], "server": p["server"]})
    characters_info = [get_characters_info(c) for c in character_to_add]

    # Removed None values
    characters_info.remove(None)

    logger.info(f"Number character to insert :{len(characters_info)}")
    logger.info(characters_info)
    if len(characters_info)>0:
        # Insert into DB
        engine = get_database_engine()
        metadata = MetaData(bind=engine)
        characters_table = Table('characters', metadata, autoload_with=engine)
        with engine.connect() as conn:
            conn.execute(characters_table.insert(), characters_info)


def get_characters_info(character)->dict:
    server = character["server"]
    name = character["name"].lower()

    url = f"https://eu.api.blizzard.com/profile/wow/character/{server}/{name}"
    hearders = {
        "Battlenet-Namespace": "profile-eu"
    }
    try: 
        r = call(url=url, headers=hearders)
        data = {
            "id": r["id"],
            "server": server,
            "name": name,
            "class": r["character_class"]["name"]["en_US"],
            "race": r["race"]["name"]["en_US"],
            "faction": r["faction"]["name"]["en_US"],
            "gender": r["gender"]["name"]["en_US"],
        }
        return data
    except Exception:
        logger.info(f"{name} cannot be fetched")


