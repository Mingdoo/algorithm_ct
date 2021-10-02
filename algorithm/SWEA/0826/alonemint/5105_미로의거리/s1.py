import sys
sys.stdin = open('sample_input.txt')


def find_route(v, checked):

    x = v[1]
    y = v[0]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    res = []
    for i in range(4):
        if 0 <= y + dy[i] < len(checked) and 0 <= x + dx[i] < N and checked[y + dy[i]][x + dx[i]] == 0:
            res.append((y + dy[i], x + dx[i]))
    return res


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    checked = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                end = (i, j)
            elif board[i][j] == 1:
                checked[i][j] = 1

    queue = [start]

    while queue:
        v = queue.pop(0)
        for y, x in find_route(v, checked):
            queue.append((y, x))
            checked[y][x] += checked[v[0]][v[1]] + 1

    print('#{} {}'.format(tc, max(0, checked[end[0]][end[1]] - 1)))