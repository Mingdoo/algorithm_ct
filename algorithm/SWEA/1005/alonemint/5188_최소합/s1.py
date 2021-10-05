import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321] * N for _ in range(N)]
    q = []
    q.append([0, 0])
    visited[0][0] = board[0][0]
    dr = [0, 1]
    dc = [1, 0]

    while q:
        v = q.pop()
        r = v[0]
        c = v[1]
        for i in range(2):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                visited[nr][nc] = min(visited[r][c] + board[nr][nc], visited[nr][nc])
                q.append([nr, nc])

    print(f'#{tc} {visited[N-1][N-1]}')