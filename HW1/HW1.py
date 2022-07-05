# 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
import requests
import json
from pprint import pprint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
params = {'q': 'name', 'id': '69846294'}
url = 'https://api.github.com'
user = 'dzhumaes'
response = requests.get(f'{url}/users/{user}/repos', headers=headers, params=params)

#Вариант 1
print('Вариант решения №1 задания №1:')
j_data = response.json()
for i in j_data:
    pprint(f"Репозитарий пользователя {user}: {i['full_name']}")

#Вариант 2
print('Вариант решения №2 задания №1:')
with open('data.json', 'w') as f:
    json.dump(response.json(), f)

for i in response.json():
    print(i['full_name'])


# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
# Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json

url = 'https://api.vk.com'
method = 'groups.get'
user_id = '8210913'
access_token = ''

responce = requests.get(f'{url}/method/{method}?v=5.131&access_token={access_token}')

with open('data.json', 'w') as f:
    json.dump(responce.json(), f)

print('Вариант решения задания №2:')
print(responce.json())

#Ответ: {'response': {'count': 49, 'items': [2215843, 26116713, 68638979, 87172081, 25117353, 31112617, 64876876, 25232578, 163215, 78812107, 32275859, 11881566, 14818302, 26877346, 27895065, 13302, 73354773, 50236893, 16768580, 18366837, 111846547, 43229227, 67869873, 44484421, 37861654, 30887439, 70898607, 14392583, 23109991, 52227503, 58814984, 128756155, 58093392, 49921137, 40442903, 3177, 30735053, 26017268, 41589556, 47554138, 46786222, 11812691, 51338099, 12947280, 10217085, 137634, 41265054, 274806, 13345493]}}