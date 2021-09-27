import requests
from pprint import pprint

url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
x_auth_token = 'df7df4c0267077ff4022af925559313f'
headers = {
    'X-Auth-Token' : x_auth_token,
}

def start(problem, headers):
    params = {
        'problem' : problem,
    }
    url_new = url + '/start'
    return requests.post(url_new, headers=headers, json=params).json()
def waiting_line(auth_key):
    url_new = url + '/waiting_line'
    headers = {
        'Authorization' : auth_key,
    }
    return requests.get(url_new, headers=headers).json()
def game_result(auth_key):
    url_new = url + '/game_result'
    headers = {
        'Authorization' : auth_key,
    }
    return requests.get(url_new, headers=headers).json()
def user_info(auth_key):
    url_new = url + '/user_info'
    headers = {
        'Authorization': auth_key,
    }
    return requests.get(url_new, headers=headers).json()
def match(auth_key, json):
    url_new = url + '/match'
    headers = {
        'Authorization': auth_key,
    }
    return requests.put(url_new, headers=headers, json=json).json()
def change_grade(auth_key, commands):
    url_new = url + '/change_grade'
    headers = {
        'Authorization': auth_key,
    }
    return requests.put(url_new, headers=headers, json=commands)
def score(auth_key):
    url_new = url + '/score'
    headers = {
        'Authorization': auth_key,
    }
    return requests.get(url_new, headers=headers).json()

'''
problem 1
auth key : start(1, headers)['auth_key']
'''

auth_key = start(1, headers)['auth_key']
#init block
N = len(user_info(auth_key)['user_info'])
grade = [{} for _ in range(N+1)]
def initialization(auth_key):
    for i in range(1, N+1):
        grade[i] = {
            'id': i,
            'grade': 1500,
        }
    command = {
        'commands' : grade[1:]
    }
    change_grade(auth_key, command)
    return


# init(모든 rank 초기화)를 하려면 아래 코드를 실행하면 됨.
initialization(auth_key)
print(grade)
# 출처 : https://ko.wikipedia.org/wiki/%EC%97%98%EB%A1%9C_%ED%8F%89%EC%A0%90_%EC%8B%9C%EC%8A%A4%ED%85%9C
K = 20

def elo_system(game_result):
    for game_set in game_result:
        winner = game_set['win']
        loser = game_set['lose']
        grade_winner = grade[winner]['grade']
        grade_loser = grade[loser]['grade']

        E_w = 1 / (1 + 10 ** ((grade_loser - grade_winner) / 400))
        E_l = 1 / (1 + 10 ** ((grade_winner - grade_loser) / 400))
        print(f'{winner}의 grade : {grade_winner} => ', end = '')
        grade[winner]['grade'] += K * E_l
        print(grade[winner]['grade'])
        print(f'{loser}의 grade : {grade_loser} => ', end='')
        grade[loser]['grade'] -= K * E_l
        print(grade[loser]['grade'])
    command = {
        'commands': grade[1:],
    }
    change_grade(auth_key, command)

def simulate(auth_key):
    #현재 기다리는 Q
    global K
    queue = waiting_line(auth_key)['waiting_line']
    for i in range(len(queue)):
        queue[i]['grade'] = queue[i].get('grade', grade[queue[i]['id']]['grade'])
    queue = sorted(queue, key=lambda x: x['grade'])

    pairs = []
    for idx in range(len(queue)):
        try:
            pairs.append([queue[2*idx]['id'], queue[2*idx+1]['id']])
            print(f'{queue[2*idx]["id"]} 와 {queue[2*idx+1]["id"]}의 매치')
        except:
            pass
    json = {
        'pairs': pairs,
    }
    res = match(auth_key, json=json)
    if res['time'] % 54 == 0:
        K *= 0.98
        print(f'!!!K의 값은 {K}!!!')
    return

while True:
    if not waiting_line(auth_key)['waiting_line']:
        print(waiting_line(auth_key)['waiting_line'])
        res = match(auth_key, json={
            'pairs': [[]],
        })
        print(res)
        if res['time'] % 54 == 0:
            K *= 0.98
            print(f'!!!K의 값은 {K}!!!')

    if len(game_result(auth_key)['game_result']):
        elo_system(game_result(auth_key)['game_result'])

    if len(waiting_line(auth_key)['waiting_line']):
        simulate(auth_key)

    if len(score(auth_key)) >= 3:
        print(score(auth_key))
        break