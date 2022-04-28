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
last = 0


def get_games(last, wrap):
    options = 'fields *; sort id asc; where id != null; where name != null; where rating != null;  ' \
              'limit {0}; offset {1};'.format(LIMIT, last)
    print('returning {0}'.format(last))
    time.sleep(1)
    return wrap.api_request('games', options)


def make_list(end: int = 1000):
    with open(os.path.join(os.getcwd(), '../Data/games.csv'), 'w', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile)
        for last in range(0, end, LIMIT):
            wr.writerows(
                [game['id'], game['name'], game['rating']]
                for game in json.loads(
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
