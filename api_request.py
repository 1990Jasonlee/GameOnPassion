import json
import urllib.request
import time


file = 0
token = 'Bearer%20awezqu488bbrfihoev5yxu4oe2h0yt'
client_id = 'tvm3g7znmadal06thlqf63p41ll5kz'

while file < 50:
    time.sleep(10)
    url = f'https://api.igdb.com/v4/games?Client-ID={client_id}&Authorization={token}%20fields%20*;'
    req = urllib.request.Request(url)
    file_name = '.games'+str(file)+'.json'

    with urllib.request.urlopen(req) as f:
        data = json.load(f)

        with open(file_name, 'w') as fo:
            json.dump(data, fo)