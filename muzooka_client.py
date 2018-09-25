import json
import os
import requests


user_token = os.environ.get('MUZZOKA_TOKEN')

muzooka_api_url = 'https://devapi.muzooka.com/v1/artists/?name={}&limit=1'


def get_artist_by_name(artist_name, spotify_id=None):

    headers = {
        'X-api-key': user_token,
    }
    request = requests.get(muzooka_api_url.format(artist_name), headers=headers)

    if spotify_id:
        for artist in json.loads(request.text)['data']:

            if 'url' in artist['social']['spotify']:
                if artist['social']['spotify'].get('url').find(spotify_id) != -1:
                    return artist, True

    return json.loads(request.text)['data'][0], False
