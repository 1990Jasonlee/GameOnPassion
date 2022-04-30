import json
import os
from igdb.wrapper import IGDBWrapper
import requests

igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')
wrapper = IGDBWrapper(igdb_id, igdb_token)
url = 'https://api.igdb.com/v4/covers'
offset = 0
limit = 500
result = 15000


def get_games_cover(offset=offset):
    while True:
        headers = {
            'Client-ID': f'{igdb_id}',
            'Authorization': f'Bearer {igdb_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'fields id, url; limit {limit}; offset {offset};'
        response = requests.post(url, headers=headers, data=data)
        print(response)
        offset += limit

        with open('../Data/data_url.json', 'a', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
            if result == offset:
                break


def correct_file_cover():
    f1 = open('../Data/data_url.json', 'r')
    input_data = f1.read()
    f1.close()

    input_data = input_data.replace('][', ',')

    f2 = open('../Data/data_url.json', 'w')
    f2.write(input_data)
    f2.close()

