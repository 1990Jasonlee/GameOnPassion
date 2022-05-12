import json
import os
from igdb.wrapper import IGDBWrapper
import requests

igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')
wrapper = IGDBWrapper(igdb_id, igdb_token)
url = 'https://api.igdb.com/v4/games'
offset = 0
limit = 500
result = 2500


# retrieve game id, name, platform, genre, game mode, release date, cover, category, ratings, summary data
def get_games(offset=offset):
    while True:
        headers = {
            'Client-ID': f'{igdb_id}',
            'Authorization': f'Bearer {igdb_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = 'fields id, aggregated_rating, aggregated_rating_count, cover, category, first_release_date, ' \
               'game_modes, genres, name, platforms, rating, rating_count, summary, total_rating, ' \
               f'total_rating_count; sort id asc; where rating >=85; limit {limit}; offset {offset};'
        response = requests.post(url, headers=headers, data=data)
        print(response)
        offset += limit

        with open('../data/data.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
            if result == offset:
                break


def correct_file_game():
    f1 = open('../data/data.json', 'r')
    input_data = f1.read()
    f1.close()

    input_data = input_data.replace('][', ',')

    f2 = open('../data/data.json', 'w')
    f2.write(input_data)
    f2.close()

