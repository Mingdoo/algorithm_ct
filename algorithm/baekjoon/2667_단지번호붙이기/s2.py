dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c):
    global number
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nc < N and 0 <= nr < N and visited[nr][nc] == 0 and board[nr][nc] == 1:
            visited[nr][nc] = 1
            number += 1
            dfs(nr, nc)

# N = int(input())
# board = [list(map(int, list(input()))) for _ in range(N)]
N = 4
board = [[1,1,0,0],[1,0,0,1],[0,0,1,1],[1,0,0,0]]
visited = [[0] * N for _ in range(N)]
res = []
num = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            num += 1
            number = 1
            dfs(i,j)
            res.append(number)
            number = 0
print(num)
for e in sorted(res):
    print(e)