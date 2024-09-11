import requests
import json
from dataclasses import dataclass, asdict
from typing import Optional
#from rich import print

BASE_URL = "https://rickandmortyapi.com/api/"
CHARACTER_URL = BASE_URL + "character/"
LOCATION_URL = BASE_URL + "location/"
EPISODE_URL = BASE_URL + "episode/"

@dataclass
class CharFilter:
    name: Optional[str] = None 
    status: Optional[str] = None
    gender: Optional[str] = None
    species: Optional[str] = None
    page: Optional[int] = None


def get_character(char_id):
    resp = requests.get(CHARACTER_URL + str(char_id)).json()
    print(json.dumps(resp, indent=4))

def search_character(search):
    resp = requests.get(CHARACTER_URL, params=search).json()
    print(json.dumps(resp, indent=2))

def main():
    search = CharFilter(
        name = "rick",
        status = "dead",
        page = 2
    )
    print(search)
    print(asdict(search))
    search_character(search=asdict(search))
   
if __name__ == "__main__":
    main()