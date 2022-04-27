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


def get_games1(last, wrap):
    options = 'fields *; sort id asc; where id != null; where cover != null; where category != null; ' \
              ' limit {0}; offset {1};'.format(LIMIT, last)

    print('returning {0}'.format(last))
    time.sleep(1)
    return wrap.api_request('games', options)


def make_list1(end: int = 1000):
    last = 0

    with open(os.path.join(os.getcwd(), 'games1.csv'), 'w', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        for last in range(0, end, LIMIT):
            wr.writerows(
                [game['id'], game['cover'], game['category']]
                for game in json.loads(
                    get_games1(last, wrapper).decode('utf-8').replace("'", '"')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_list1(int(sys.argv[1]))
    else:
        make_list1()
