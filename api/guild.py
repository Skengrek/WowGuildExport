"""
Get all information about a guild
"""
from .utils import call
BASE_URL = "https://eu.api.blizzard.com/data/wow" 

def get_info(server: str, name: str):
    url = f"{BASE_URL}/guild/{server}/{name}"
    request =  call(url)
    print(request.json())


if __name__ == "__main__":
    get_info("garona", "ascencia")