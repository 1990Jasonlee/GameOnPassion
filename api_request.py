import csv
import json
import sys
import time
import urllib.request
import os
from igdb.wrapper import IGDBWrapper

file = 0
igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')

wrapper = IGDBWrapper(igdb_id, igdb_token)
byte_array = wrapper.api_request(
    'games',
    'fields id, name, genres, rating; offset 0; where platforms=48;',
)

LIMIT = 4


def get_games(last, wrap):
    options = 'fields id, name, age_ratings, aggregated_rating, aggregated_rating_count, cover, first_release_date, ' \
              'genres, multiplayer_modes, rating, rating_count, storyline, total_rating, total_rating_count;' \
              ' limit {0}; offset {1};'.format(LIMIT, last)
    print('last was {0}'.format(last))
    time.sleep(1)
    return wrap.api_request('games', options)


def make_list(end: int = 10000):
    last = 0

    with open(
            os.path.join(os.getcwd(), 'game_titles.csv'),
            'w',
            newline='',
            encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        for last in range(0, end, LIMIT):
            wr.writerows(
                [item['name']]
                for item in json.loads(
                    get_games(last, wrapper).decode('utf-8').replace("'", '"')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_list(int(sys.argv[1]))
    else:
        make_list()

# while file < 2:
#     url = f'https://api.igdb.com/v4/games?Client-ID={igdb_id}&Authorization=Bearer%20{igdb_token}%20fields%20*;'
#     req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#     webpage = urllib.request.urlopen(req, timeout=10).read()
#     file_name = '.games' + str(file) + '.json'
#
#     with urllib.request.urlopen(req) as f:
#         data = json.load(f)
#
#         with open(file_name, 'w') as fo:
#             json.dump(data, fo)
