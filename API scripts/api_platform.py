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


def get_games(last, wrap):
    options = 'fields *; limit {0}; offset {1};'.format(LIMIT, last)

    print('returning {0}'.format(last))
    time.sleep(1)
    return wrap.api_request('platforms', options)


def make_list(end: int = 200):
    last = 0

    with open(os.path.join(os.getcwd(), '../Data/platforms.csv'), 'w', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        for last in range(0, end, LIMIT):
            wr.writerows(
                [game['name']]
                for game in json.loads(
                    get_games(last, wrapper).decode('utf-8').replace("'", '"')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        make_list(int(sys.argv[1]))
    else:
        make_list()
