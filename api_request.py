import csv
import json
import sys
import time
import os
from igdb.wrapper import IGDBWrapper

file = 0
igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')

wrapper = IGDBWrapper(igdb_id, igdb_token)
LIMIT = 4


def get_games(last, wrap):
    options = 'fields id, name, age_ratings, aggregated_rating, aggregated_rating_count, cover, first_release_date, ' \
              'genres, multiplayer_modes, platforms, rating, rating_count, storyline, total_rating, total_rating_count;' \
              ' limit {0}; offset {1};'.format(LIMIT, last)
    print('returning {0}'.format(last))
    time.sleep(1)
    return wrap.api_request('games', options)


def make_list(end: int = 10):
    last = 0

    with open(
            os.path.join(os.getcwd(), 'games.csv'),
            'w',
            newline='',
            encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        for last in range(0, end, LIMIT):
            wr.writerows(
                [item['name'], item['id']]
                for item in json.loads(
                    get_games(last, wrapper).decode('utf-8').replace("'", '"')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_list(int(sys.argv[1]))
    else:
        make_list()
