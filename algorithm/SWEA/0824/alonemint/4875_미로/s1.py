import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    checked = [[0] * N for _ in range(N)]
    board = [list(map(int, list(input()))) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                start = (i, j)
            elif board[i][j] == 3:
                end = (i, j)
            elif board[i][j] == 1:
                checked[i][j] = 1

    stack = []
    #우하좌상
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    #DFS 구현
    stack = [start]

    boolean = False
    while stack:
        v = stack.pop()
        y = v[0]
        x = v[1]
        checked[y][x] = 1
        if checked[end[0]][end[1]]:
            boolean = True
            break
        #2차원배열 index조건
        for i in range(4):
            if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and checked[y + dy[i]][x + dx[i]] == 0:
                stack.append((y + dy[i], x + dx[i]))

    #출력
    if boolean:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))