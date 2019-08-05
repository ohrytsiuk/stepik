from operator import itemgetter

import requests
import json

client_id = '1fac7e6508a55f5dce1a'
client_secret = 'd128be717407abb4e7a057f19f471aa0'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

with open('dataset_24476_4.txt', encoding='UTF-8') as file:
    data = file.readlines()

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком
da = {}
for id in data:
    r = requests.get("https://api.artsy.net/api/artists/{id}".format(id=id.rstrip()), headers=headers)
    r.encoding = 'utf-8'

    # разбираем ответ сервера
    j = json.loads(r.text)
    da[j.get('sortable_name')] = j.get('birthday')

da = sorted(da.items(), key=itemgetter(1, 0))

for key, value in da:
    print(key)
