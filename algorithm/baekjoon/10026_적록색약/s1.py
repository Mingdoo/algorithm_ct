from collections import deque
# import sys
# sys.stdin = open('input.txt')
N = int(input())

board = [list(input()) for _ in range(N)]
normal = [[0] * N for _ in range(N)]
abnormal = [[0] * N for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

stack = deque()
normal_cnt = 0
color = ''
for i in range(N):
    for j in range(N):
        if normal[i][j] == 0:
            stack.append([i,j])
            color = board[i][j]
            normal_cnt += 1
            while stack:
                v = stack.pop()
                for k in range(4):
                    nr = v[0] + dr[k]
                    nc = v[1] + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color and normal[nr][nc] == 0:
                        normal[nr][nc] = 1
                        stack.append([nr, nc])

for i in range(N):
    for j in range(N):
        if board[i][j] == 'R':
            board[i][j] = 'G'

stack = deque()
color = ''
abnormal_cnt = 0
for i in range(N):
    for j in range(N):
        if abnormal[i][j] == 0:
            stack.append([i,j])
            color = board[i][j]
            abnormal_cnt += 1
            while stack:
                v = stack.pop()
                for k in range(4):
                    nr = v[0] + dr[k]
                    nc = v[1] + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color and abnormal[nr][nc] == 0:
                        abnormal[nr][nc] = 1
                        stack.append([nr, nc])
print(normal_cnt, abnormal_cnt)