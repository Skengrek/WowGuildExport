from pandas import DataFrame
from logging import getLogger
from datetime import datetime
from sqlalchemy.orm import Session
from wowexport.utils import get_database_engine
from airflow.decorators import task, task_group
from sqlalchemy import Table, MetaData, engine, select, func
logger = getLogger(__name__)


@task_group
def activity_task_group(activity: list):
    a = activity_response_to_list(activity)
    insert_new_activities(a)
    return a

@task
def activity_response_to_list(activity_response: dict)-> list:
    activities = []
    for act in activity_response["activities"]:
        if "character_achievement" in act:
            activities.append({
                "type": act["activity"]["type"],
                "name": act["character_achievement"]["achievement"]["name"]["en_US"],
                "id": act["character_achievement"]["achievement"]["id"],
                "player_id": act["character_achievement"]["character"]["id"],
                "timestamp": act["timestamp"]
            })
        elif "encounter_completed" in act:
            activities.append({
                "type": act["encounter_completed"]["mode"]["type"],
                "name": act["encounter_completed"]["encounter"]["name"]["en_US"],
                "id": act["encounter_completed"]["encounter"]["id"],
                "player_id": None,
                "timestamp": act["timestamp"]
            })
    return activities


@task
def insert_new_activities(activities):
    engine = get_database_engine()
    metadata = MetaData(bind=engine)
    activity_table = Table('activities', metadata, autoload_with=engine)
    last_date = get_last_activity_datetime(activity_table, engine)

    # Create dataframe
    activity_df = DataFrame(activities)
    activity_df["datetime"] = activity_df["timestamp"].apply(timestamp_to_datetime)

    if last_date is not None:
        activity_df = activity_df[activity_df["datetime"]>last_date]
    
    activity_df = activity_df.rename(columns={"id": "activity_id"})
    activity_records = activity_df.to_dict(orient='records')

    logger.info(activity_df.columns)
    with engine.connect() as conn:
        conn.execute(activity_table.insert(), activity_records)


def get_last_activity_datetime(table: Table, engine: engine) -> datetime:
    with Session(engine) as session:
        # Construct the query to get the max value of a datetime column
        max_datetime = session.execute(
            select(func.max(table.c.datetime))
        ).scalar()
        return max_datetime


def timestamp_to_datetime(x):
    return datetime.fromtimestamp(x/1000)