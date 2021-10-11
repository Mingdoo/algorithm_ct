import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

def dfs(r, c, ans):
    global maximum
    maximum = max(ans, maximum)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and visited[board[nr][nc]] == 0:
            visited[board[nr][nc]] = 1
            dfs(nr, nc, ans+1)
            visited[board[nr][nc]] = 0

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
visited = [0] * 26
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

maximum = 0

visited[board[0][0]] = 1
dfs(0, 0, 1)
print(maximum)