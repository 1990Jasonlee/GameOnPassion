import json
import os
from igdb.wrapper import IGDBWrapper
import requests

igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')
wrapper = IGDBWrapper(igdb_id, igdb_token)
url = 'https://api.igdb.com/v4/game_modes'
offset = 0
limit = 10
result = 10


# retrieve game mode info
def get_gamesmode(offset=offset):
    while True:
        headers = {
            'Client-ID': f'{igdb_id}',
            'Authorization': f'Bearer {igdb_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'fields id, name; sort id asc; limit {limit}; offset {offset};'
        response = requests.post(url, headers=headers, data=data)
        print(response)
        offset += limit

        with open('../data/data_gamemode.json', 'w', encoding='utf-8') as f:

            json.dump(response.json(), f, ensure_ascii=False, indent=4)
            if result == offset:
                break
