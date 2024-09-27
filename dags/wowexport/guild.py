from .utils import call
from logging import getLogger
from airflow.decorators import task, task_group
logger = getLogger(__name__)

@task_group(group_id="guild")
def guild_task_group():
    a = information()
    b = activity()
    c = roster()
    return {"information": a, "activity": b, "roster": c}

@task()
def information(server="garona", name="ascencia"):
    return call(
        f"https://eu.api.blizzard.com/data/wow/guild/{server}/{name}",
        headers={"Battlenet-Namespace": "profile-eu"}
    )


@task()
def activity(server="garona", name="ascencia"):
    r = call(
        f"https://eu.api.blizzard.com/data/wow/guild/{server}/{name}/activity",
        headers={"Battlenet-Namespace": "profile-eu"}
    )
    logger.info(r)
    return r


@task()
def roster(server="garona", name="ascencia"):
    return call(
        f"https://eu.api.blizzard.com/data/wow/guild/{server}/{name}/roster",
        headers={"Battlenet-Namespace": "profile-eu"}
    )