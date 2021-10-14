import sys
sys.stdin = open('sample_input.txt')
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[1e9] * N for _ in range(N)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                h_diff = max(board[nr][nc] - board[r][c], 0)
                if visited[nr][nc] > visited[r][c] + h_diff + 1:
                    visited[nr][nc] = visited[r][c] + h_diff + 1
                    q.append([nr, nc])
    print(f'#{tc} {visited[N-1][N-1]}')


