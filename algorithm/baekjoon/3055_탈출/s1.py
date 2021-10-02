import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited2 = [[0] * M for _ in range(N)]
waters = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 'S':
            start_ = [i,j]
        if board[i][j] == 'D':
            end = [i,j]
            visited[i][j] = 123456789
        if board[i][j] == '*':
            waters.append([i,j])
        if board[i][j] == 'X':
            visited[i][j] = 987654321

q = deque()
q2 = deque()

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for water in waters:
    q2.append(water)
    visited[water[0]][water[1]] = 1
while q2:
    start = q2.popleft()
    for i in range(4):
        if 0 <= start[0] + dr[i] < N and 0 <= start[1] + dc[i] < M:
            if visited[start[0] + dr[i]][start[1] + dc[i]] == 0 or visited[start[0] + dr[i]][start[1] + dc[i]] > visited[start[0]][start[1]] + 1:
                if visited[start[0] + dr[i]][start[1] + dc[i]] != 987654321 and visited[start[0] + dr[i]][start[1] + dc[i]] != 123456789:
                    visited[start[0] + dr[i]][start[1] + dc[i]] = visited[start[0]][start[1]] + 1
                    q2.append([start[0] + dr[i], start[1] + dc[i]])

print(visited)
q.append(start_)
visited2[start_[0]][start_[1]] = 1
while q:
    start = q.popleft()
    for i in range(4):
        if 0 <= start[0]+dr[i] < N and 0 <= start[1]+dc[i] < M:
            if (visited2[start[0]+dr[i]][start[1]+dc[i]] > visited2[start[0]][start[1]] + 1 and visited2[start[0]+dr[i]][start[1]+dc[i]] != 987654321) or visited[start[0]+dr[i]][start[1]+dc[i]] == 0:
                visited2[start[0]+dr[i]][start[1]+dc[i]] = visited2[start[0]][start[1]] + 1
                q.append([start[0]+dr[i], start[1]+dc[i]])
            elif visited2[start[0]+dr[i]][start[1]+dc[i]] == 123456789:
                visited2[start[0] + dr[i]][start[1] + dc[i]] = visited2[start[0]][start[1]] + 1
                q.append([start[0]+dr[i], start[1]+dc[i]])
print(visited2)
print(visited[end[0]][end[1]] - 1 if visited[end[0]][end[1]] < 123456789 else 'KAKTUS')