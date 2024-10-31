import requests
from logging import getLogger
from sqlalchemy import create_engine
from airflow.hooks.base import BaseHook

logger = getLogger(__name__)

def get_token()-> dict:
    conn = BaseHook.get_connection("WARCRAFTLOGSAPI")
    logger.info(conn.login)
    logger.info(conn.password)
    response = requests.post(
        "https://www.warcraftlogs.com/oauth/token",
        auth=(conn.login, conn.password),
        data={"grant_type":"client_credentials"}    
    )
    logger.info("Got Access token")
    return response.json()["access_token"]


def call(url: str)-> dict:
    conn = BaseHook.get_connection("WARCRAFTLOGSAPI")
    resp = requests.get(
        url,
        params={"api_key": conn.password}
    ).json()
    return resp
