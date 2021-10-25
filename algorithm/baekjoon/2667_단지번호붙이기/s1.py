N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

#우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

stack = []
res = []
number = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and board[i][j] == 1:
            number += 1
            stack.append([i, j])
            visited[i][j] = number
            num = 0
            while stack:
                v = stack.pop()
                num += 1
                r, c = v[0], v[1]
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] == 1:
                        visited[nr][nc] = number
                        stack.append([nr, nc])
            res.append(num)

# from pprint import pprint
# pprint(visited)

print(number)
for element in sorted(res):
    print(element)