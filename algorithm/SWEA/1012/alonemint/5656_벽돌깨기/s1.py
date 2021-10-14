import sys
sys.stdin = open('sample_input.txt')

from copy import deepcopy
from itertools import product
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def gravity(arr):
    for x in range(W):
        tmp = H - 1
        for y in range(H - 1, -1, -1):
            if arr[y][x]:
                if tmp != y:
                    arr[tmp][x], arr[y][x] = arr[y][x], arr[tmp][x]
                tmp -= 1
    return arr

def brick_breaker(arr, n):
    arr = deepcopy(arr)
    start = [-1, -1]
    for j in range(H):
        if arr[j][n] != 0:
            start = [j, n]
            break
    if start == [-1, -1]:
        return 0, 0
    q = deque([start])
    while q:
        v = q.popleft()
        power = arr[v[0]][v[1]]
        arr[v[0]][v[1]] = 0
        for i in range(4):
            for j in range(1, power):
                nr = v[0] + dr[i] * j
                nc = v[1] + dc[i] * j
                if 0 <= nr < H and 0 <= nc < W:
                    q.append([nr, nc])
    tmp = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] != 0:
                tmp += 1
    return gravity(arr), tmp

for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    answer = 1e9
    for prod in product(range(W), repeat=N):
        tmp = 1e9
        arr = deepcopy(board)
        for i in prod:
            if tmp:
                arr, tmp = brick_breaker(arr, i)
        answer = min(answer, tmp) if arr and tmp >= 0 else answer

    print(f'#{tc} {answer}')