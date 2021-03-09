# Задание 1.
# Посмотреть документацию к API GitHub,
# разобраться как вывести список репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.

import requests
import json


base_url = 'https://api.github.com'
username = 'PetrovNikA'

req = requests.get(f'{base_url}/users/{username}/repos')

# json-данные:
if req.ok:
    data = req.json()

# Вывод списка:
for n in data:
    print(n['name'])

# Сохранение в файл:
if req.ok:
    with open('parse_rep_list.json', 'w') as f:
        json.dump(data, f)
