import sys
from collections import deque
# sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
water_visited = [[-1] * M for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            start = [i,j]
            visited[i][j] = 0
            board[i][j] = '.'
        if board[i][j] == 'D':
            end = [i,j]
        if board[i][j] == '*':
            q.append([i,j])
            water_visited[i][j] = 0



dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == '.' and water_visited[nr][nc] == -1:
            water_visited[nr][nc] = water_visited[r][c] + 1
            q.append([nr, nc])
# print(water_visited)
q.append(start)
while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] in '.D' and visited[nr][nc] == -1:
            if visited[r][c] + 1 < water_visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])
            elif water_visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append([nr, nc])

if visited[end[0]][end[1]] == -1:
    print('KAKTUS')
else:
    print(visited[end[0]][end[1]])