import time
import requests
from pprint import pprint
import json

# TOKEN = 'vk1.a.xGngL8Ju9ZI96uSb6wEYrFXpbIbyeGSoMXDcoxJwLiwhFNFoNgE8N-k6nB-2vxdWrDd8CH-1g3L6CNbzZ2YaSDItsVSsTeES5SS1GX5j1KVxX_YtBSMPoSFJoHq5gS3nZ-h0k3e1PhrFE4vfiZPgfvpmZ9Xgxw0dW0PgJGLI5nPWxC7BwQAji5MdfkpO-xfb'

def test_get_photo():
    url_vk = 'https://api.vk.com/method/photos.get'
    params_vk = {
        'user_ids': '12541943',
        'access_token': 'vk1.a.xGngL8Ju9ZI96uSb6wEYrFXpbIbyeGSoMXDcoxJwLiwhFNFoNgE8N-k6nB-2vxdWrDd8CH-1g3L6CNbzZ2YaSDItsVSsTeES5SS1GX5j1KVxX_YtBSMPoSFJoHq5gS3nZ-h0k3e1PhrFE4vfiZPgfvpmZ9Xgxw0dW0PgJGLI5nPWxC7BwQAji5MdfkpO-xfb',
        'v': '5.131',
        'owner_id': '12541943',
        'album_id': 'profile',
        'extended': '1',
        'count': '3',

    }
    response = requests.get(url_vk, params=params_vk)
    x = json.loads(response.text)
    return x

v = test_get_photo()
# pprint(v['response']['items'][0])
list_photo = []
for data_photo in v['response']['items']:
    the_first_value = 0
    dict_photo = {}
    dict_parameters_photo = {}
    name_photo = data_photo['likes']['count']
    dict_photo.setdefault('likes', name_photo)
    for parameters_photo in data_photo['sizes']:
        average_value = ((parameters_photo['height'] + parameters_photo['width'])/2)
        if average_value > the_first_value:
            the_first_value = average_value
            type_photo = parameters_photo['type']
            url_photo = parameters_photo['url']
        else:
            the_first_value = average_value
    dict_parameters_photo.setdefault('likes', name_photo)
    dict_photo.setdefault('type', type_photo)
    dict_photo.setdefault('url', url_photo)
    list_photo.append(dict_photo)
pprint(list_photo)



    # def creature_json_photo():
#     for element_T2 in response.json()
#     response = json{}
#     test_get_photo()
#     x = response.json()
#     pprint(x)
#
# creature_json_photo()
#
# json_photo = {
#     'name': '',
#     'url': ''
# }








