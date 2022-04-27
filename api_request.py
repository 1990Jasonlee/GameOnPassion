import json
import urllib.request
import time
import os

file = 0
igdb_token = os.environ.get('IGDB_TOKEN')
igdb_id = os.environ.get('IGDB_ID')



# while file < 50:
#     time.sleep(10)
#     url = f'https://api.igdb.com/v4/games?Client-ID={client_id}&Authorization={token}%20fields%20*;'
#     req = urllib.request.Request(url)
#     file_name = '.games'+str(file)+'.json'
#
#     with urllib.request.urlopen(req) as f:
#         data = json.load(f)
#
#         with open(file_name, 'w') as fo:
#             json.dump(data, fo)