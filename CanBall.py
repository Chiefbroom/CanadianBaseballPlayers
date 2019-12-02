import json
import requests

api_url_base = ''
headers ={'Content-Type': 'application/json'}

def get_albumtracks():
    api_url = '{0}'.format(api_url_base)

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

album_info = get_albumtracks()

if album_info is not None:
    print("Here's your info: ")
    for album in album_info.items():
        print(album)

else:
        print('[!] Request Failed')
