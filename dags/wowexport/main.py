from datetime import datetime
from airflow.models.dag import DAG
from wowexport.blizzard.guild import guild_task_group
from wowexport.blizzard.player import player_task_group
from wowexport.blizzard.activity import activity_task_group

from wowexport.warcraftlogs.guild import get_raid_data



with DAG(dag_id="guild_scrapping", tags=["wow"], catchup=False, start_date=datetime(2024,1,1))as dag:
    a = guild_task_group()
    b = player_task_group(a["roster"])
    c = activity_task_group(a["activity"])

    d = get_raid_data()

