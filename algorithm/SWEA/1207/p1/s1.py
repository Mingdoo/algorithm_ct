import sys
from pprint import pprint
sys.stdin = open('input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(T):
    M, N, L = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(M)]
    visited = [[1e9] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                end = (i, j)

    stack = [[start, L, 0]]
    while stack:
        q = stack.pop()
        r, c = q[0]
        cnt = q[2]
        if q[1] == 0:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr in range(M) and nc in range(N) and visited[nr][nc] == 1e9:
                visited[nr][nc] = cnt
                if board[nr][nc] == 1:
                    visited[nr][nc] = cnt + 1
                    stack.append([(nr, nc), L, cnt+1])
                else:
                    stack.append([(nr, nc), L-1, cnt])
    pprint(visited)




