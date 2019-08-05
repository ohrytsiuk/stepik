import requests

tmp_url = 'http://numbersapi.com/{number}/math?json=true'
params = {}
numbers = []
with open('dataset_24476_3.txt') as file:
    file_data = file.readlines()

for number in file_data:
    url = tmp_url.format(number=number.rstrip())
    data = requests.get(url, timeout=5)
    json = data.json()
    if json.get('found'):
        print('Interesting')
    else:
        print('Boring')
