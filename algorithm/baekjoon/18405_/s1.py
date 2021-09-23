import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X_, Y_ = map(int, input().split())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for _ in range(S):
        res = [[] for _ in range(K+1)]
        for j in range(N):
            for k in range(N):
                    for l in range(4):
                        if 0 <= j + dr[l] < len(board) and 0 <= k + dc[l] < len(board):
                            if board[j+dr[l]][k+dc[l]] != 0:
                                res[board[j+dr[l]][k+dc[l]]].append([j+dr[l],k+dc[l]])
        for p in range(1, K+1):
            for y, x in res[p]:
                board[y][x]=p
print(board[X_-1][Y_-1])

