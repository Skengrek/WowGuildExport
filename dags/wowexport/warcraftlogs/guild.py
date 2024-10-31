from .utils import call
from logging import getLogger
from datetime import datetime
from airflow.hooks.base import BaseHook
from airflow.decorators import task, task_group
logger = getLogger(__name__)

@task_group
def get_raid_data():
    a = get_guild_fights_ids()
    b = get_fights_report(a)
    return b


@task
def get_guild_fights_ids():
    conn = BaseHook.get_connection("GUILD")
    region = "EU"
    name = conn.login
    server = conn.password
    url = f"https://www.warcraftlogs.com:443/v1/reports/guild/{name}/{server}/{region}"
    resp = call(url)
    ids = [[a["id"], datetime.fromtimestamp(a["start"]/1000)] for a in resp]
    logger.info(ids)
    return ids


@task
def get_fights_report(fights_data: list):
    for data in fights_data:
        url = f"https://www.warcraftlogs.com:443/v1/report/fights/{data[0]}/"
        resp = call(url)
        logger.info(resp)