import requests
import json
import os

base_url = 'https://api.themoviedb.org/3/movie'
data = {
    'api_key': '2f3c9cee84d1fd74cfd60f2ddc95418f',
    'language': 'ko-KR'
}
my_dict = {}
my_set = set()
file = open('movies.json', encoding='UTF-8')
for i in range(1):
    line = file.readline()
    json_data = json.loads(line)
    id = json_data.get('id')
    print(json_data)
    print(json_data.get('genres'))
    response = requests.get(base_url + f'/{id}', params=data).json()
    my_dict[id] = response
    if not i % 100:
        print(i)

