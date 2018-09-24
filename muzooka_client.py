import os
import json

import requests


user_token = os.environ.get('MUZZOKA_TOKEN')

muzooka_api_url = 'https://devapi.muzooka.com/v1/artists/?name={}&limit=1'


def get_artist_by_name(artist_name):

    headers = {
        'X-api-key': user_token,
    }
    request = requests.get(muzooka_api_url.format(artist_name), headers=headers)

    return json.loads(request.text)['data'][0]
