import os
import dotenv
import requests

dotenv.load_dotenv()


def get_token()-> str:
    return requests.post(
        "https://oauth.battle.net/token",
        auth=(os.environ.get("WOW_CLIENT_ID"), os.environ.get("WOW_CLIENT_SECRET")),
        params={"grant_type":"client_credentials"}    
    ).json()["access_token"]


def call(url: str) -> dict:
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    breakpoint()
    return requests.get(url, headers=headers)