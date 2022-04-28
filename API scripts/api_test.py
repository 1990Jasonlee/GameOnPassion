import csv
import json
import sys
import time
import os

import requests as requests
from igdb.wrapper import IGDBWrapper
import requests

file = 0
igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')

wrapper = IGDBWrapper(igdb_id, igdb_token)
LIMIT = 4
last = 0


headers = {
    'Client-ID': f'{igdb_id}',
    'Authorization': f'Bearer {igdb_token}',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = 'fields alpha_channel,animated,checksum,game,height,image_id,url,width;'
print('returning {0}'.format(last))
time.sleep(1)
response = requests.post('https://api.igdb.com/v4/covers', headers=headers, data=data)

with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(response.json(), f,ensure_ascii=False, indent=4)


# def get_games(last, wrap):
#     options = 'fields *; sort id asc; where id != null; where name != null; where rating != null;  ' \
#               'limit {0}; offset {1};'.format(LIMIT, last)
#     print('returning {0}'.format(last))
#     time.sleep(1)
#     return wrap.api_request('games', options)


# def make_list(end: int = 1000):
#     with open(os.path.join(os.getcwd(), '../Data/games.csv'), 'w', newline='', encoding='utf-8') as myfile:
#         wr = csv.writer(myfile)
#         for last in range(0, end, LIMIT):
#             wr.writerows(
#                 [game['id'], game['name'], game['rating']]
#                 for game in json.loads(
#                     get_games(last, wrapper).decode('utf-8').replace("'", '"')))
#
#
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         make_list(int(sys.argv[1]))
#     else:
#         make_list()
