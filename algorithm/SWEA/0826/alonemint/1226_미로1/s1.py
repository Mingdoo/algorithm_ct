import sys
sys.stdin = open('input.txt')

T = 10

def find_route(v, visited):

    x = v[1]
    y = v[0]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    res = []

    for i in range(4):
        if 0 <= y + dy[i] < len(visited) and 0 <= x + dx[i] < len(visited) and visited[y + dy[i]][x + dx[i]] == 0:
            res.append((y + dy[i], x + dx[i]))
    return res

for tc in range(1, T + 1):
    N = input()

    size = 16
    board = [list(map(int, input())) for _ in range(size)]
    visited = [[0] * size for _ in range(size)]


    for i in range(size):
        for j in range(size):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                end = (i, j)
            elif board[i][j] == 1:
                visited[i][j] = 1

    stack = [start]

    boolean = 0

    while stack:
        v = stack.pop()
        vx = v[1]
        vy = v[0]
        if (vy, vx) == end:
            boolean = 1
            break
        if visited[vy][vx] == 0:
            visited[vy][vx] = 1

        for y, x in find_route(v, visited):
            stack.append((y,x))
            visited[y][x] = 1

    print('#{} {}'.format(tc, boolean))


