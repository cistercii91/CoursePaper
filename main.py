import time
import requests
from pprint import pprint
import json
import pathlib
from pathlib import Path
import os

params_vk = {
    'user_ids': '12541943',
    'access_token': 'vk1.a.xGngL8Ju9ZI96uSb6wEYrFXpbIbyeGSoMXDcoxJwLiwhFNFoNgE8N-k6nB-2vxdWrDd8CH-1g3L6CNbzZ2YaSDItsVSsTeES5SS1GX5j1KVxX_YtBSMPoSFJoHq5gS3nZ-h0k3e1PhrFE4vfiZPgfvpmZ9Xgxw0dW0PgJGLI5nPWxC7BwQAji5MdfkpO-xfb',
    'v': '5.131',
    'owner_id': '12541943',
    'album_id': 'profile',
    'extended': '1',
    'count': '3',
}
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

# чтение данных с сервера, их сортировка и запись в переменную
def training_parsing():
    v = test_get_photo()
    dick_photo_library = {'photo_library':{}}
    id_photo = 0
    for data_photo in v['response']['items']:
        the_first_value = 0
        dict_photo = {}
        name_photo = id_photo
        dict_photo.setdefault('likes', data_photo['likes']['count'])
        for parameters_photo in data_photo['sizes']:
            average_value = ((parameters_photo['height'] + parameters_photo['width'])/2)
            if average_value > the_first_value:
                the_first_value = average_value
                type_photo = parameters_photo['type']
                url_photo = parameters_photo['url']
            else:
                the_first_value = average_value
        dict_photo.setdefault('type', type_photo)
        dict_photo.setdefault('url', url_photo)
        dict_photo.setdefault('date', data_photo['date'])
        dick_photo_library['photo_library'].setdefault(name_photo, dict_photo)
        id_photo += 1
    y = dick_photo_library
    return y

# Функция определния уникальности количества лайков и создания имени в параметрах фотографий
def name_photo_id():
    dict_photo = training_parsing()
    list_likes = []
    non_unique_values = []
    for name in dict_photo.values():
        for name2 in name.values():
            # print('-------------')
            list_likes.append(name2['likes'])
    list_likes_len = len(list_likes)
    for i in range(0, list_likes_len-1):
        for j in range(i+1, list_likes_len):
            if list_likes[i] == list_likes[j]:
                non_unique_values.append(list_likes[i])
    for name in dict_photo.values():
        i = 0
        ban = {}
        for name2 in name.values():
            if name2['likes'] not in non_unique_values:
                name2.setdefault('name', (name2['likes']))
            else:
                name2.setdefault('name', (str(name2['likes']) + str(name2['date'])))
            ban.setdefault(list(name.keys())[i], name2)
            i += 1
    dict_photo['photo_library'] = ban
    return dict_photo


# Функция создания json. Создает так же папку отдельную для таких файлов и переносит файлы туда
def created_file():
    name = "".join(['data_photo_', params_vk['user_ids'], '.json'])
    index = 'h\h'
    w = index[1]
    dir_path = pathlib.Path.cwd()
    t = str(dir_path) + str(w) + 'photo_library' + str(w) + str(name)
    d = str(dir_path) + w + name
    if not os.path.isdir('photo_library'):
         os.mkdir('photo_library')
    check_file = os.path.exists(str(t))
    if check_file != True:
        os.path.join('photo_library', name)
        with open(name, "w+", encoding='utf-8') as write_file:
            json.dump(name_photo_id(), write_file)
    #     f = open(t, 'r')
    #     f.close()
        os.rename(d, t)
    #     f = open(t, "r")
    #     f.close()
    # f = open(t, 'r')
    # f.close()
    # name.close()
    # else:
    #     print('уже есть файл')
    # print(t)
    # return t

created_file()



    # print(dir_path)
    # print(path)



# training_parsing()

'------------------------------'
# def name_photo_id():
#     u = created_file()
#     with open(u, "w") as read_file:
#         # dict_photo = {}
#         dict_photo = json.load(read_file)['photo_library']
#     list_likes = []
#     non_unique_values = []
#     pprint(dict_photo)
#     for name in dict_photo.values():
#         print('-------------')
#         # pprint(name)
#         list_likes.append(name['likes'])
#     list_likes_len = len(list_likes)
#     for i in range(0, list_likes_len-1):
#         for j in range(i+1, list_likes_len):
#             if list_likes[i] == list_likes[j]:
#                 non_unique_values.append(list_likes[i])
#     # for x in dict_photo.keys():
#     for name in dict_photo.values():
#         if name['likes'] not in non_unique_values:
#             name.setdefault('name', (str(name['likes']) + str(name['date'])))
#             dict_photo.update(name)
#             # h = json.load(read_file)['photo_library'][name]
#             # h.setdefault('name', (name['likes'] + name['date']))
#             # pprint(dict_photo.values())
#         # print(x)
#         # print('-------------')
#         pprint(dict_photo.values())
'------------------------------'


# def name_photo_id():
#     y = training_parsing()
#     list_likes = []
#     for name in y['photo_library'].values():
#         print('-------------')
#         pprint(name)
#         list_likes.append(name['likes'])
#     list_likes_len = len(list_likes)
#     for i in range(0, list_likes_len-1):
#         for j in range(i+1, list_likes_len):
#             if list_likes[i] == list_likes[j]:
#
#                 print(j)






