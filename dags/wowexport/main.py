from datetime import datetime
from airflow.models.dag import DAG
from wowexport.guild import guild_task_group
from wowexport.player import player_task_group
from wowexport.activity import activity_task_group



with DAG(dag_id="guild_scrapping", tags=["wow"], catchup=False, start_date=datetime(2024,1,1))as dag:
    a = guild_task_group()
    b = player_task_group(a["roster"])
    c = activity_task_group(a["activity"])