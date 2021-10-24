import sys
sys.stdin = open('input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, cnt):
    if cnt > 2:
        return
    else:
        for i in range(4):
            flag = False
            dist = 51
            for j in range(1, N):
                nr = r + dr[i] * j
                nc = c + dc[i] * j
                if nr not in range(N) or nc not in range(N):
                    break
                else:
                    if board[nr][nc] == 1:
                        flag = True
                        dist = j
                        break
            if flag:
                for k in range(dist + 1, N):
                    nr = r + dr[i] * k
                    nc = c + dc[i] * k
                    if 0 <= nr < N and 0 <= nc < N:
                        if board[nr][nc] == 1:
                            board[nr][nc] = 0
                            result.add((nr,nc))
                            dfs(nr, nc, cnt+1)
                            board[nr][nc] = 1
                            break
                        elif board[nr][nc] == 0:
                            dfs(nr, nc, cnt+1)
                    else:
                        break

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                r, c = i, j
    result = set()
    dfs(r, c, 0)

    print('#{} {}'.format(tc, len(result)))