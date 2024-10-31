import requests
from sqlalchemy import create_engine
from airflow.hooks.base import BaseHook

from logging import getLogger
logger = getLogger(__name__)

def get_token()-> dict:
    conn = BaseHook.get_connection("BLIZZARDAPI")
    response = requests.post(
        "https://oauth.battle.net/token",
        auth=(conn.login, conn.password),
        params={"grant_type":"client_credentials"}    
    )
    logger.info("Got Access token")
    return response.json()["access_token"]


def call(url: str, headers:dict = None) -> dict:
    token = get_token()
    if headers is None:
        headers = {}
    headers["Authorization"] = f"bearer {token}"
    logger.info(f"Call {url}")
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        raise Exception(f"Request status code {resp.status_code}\n response:{resp.content}")
    return resp.json()


def get_database_engine():
    conn = BaseHook.get_connection("WOWGUILDEXPORTDATABASE")
    conn_str = f"postgresql+psycopg2://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}"
    return create_engine(conn_str)