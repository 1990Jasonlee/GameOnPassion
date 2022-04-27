import csv
import json
import sys
import time
import os
from igdb.wrapper import IGDBWrapper

igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')

wrapper = IGDBWrapper(igdb_id, igdb_token)
LIMIT = 4


def get_games5(last, wrap):
    options = 'fields *; sort id asc; where id != null; where total_rating != null; where total_rating_count != null; ' \
              ' limit {0}; offset {1};'.format(LIMIT, last)

    print('returning {0}'.format(last))
    time.sleep(1)
    return wrap.api_request('games', options)


def make_list5(end: int = 1000):
    last = 0

    with open(os.path.join(os.getcwd(), 'games5.csv'), 'w', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        for last in range(0, end, LIMIT):
            wr.writerows(
                [game['id'], game['total_rating'], game['total_rating_count']]
                for game in json.loads(
                    get_games5(last, wrapper).decode('utf-8').replace("'", '"')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_list5(int(sys.argv[1]))
    else:
        make_list5()
