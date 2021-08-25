import sys
sys.stdin = open('input.txt')

def find_route(start, checked):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x = start[1]
    y = start[0]

    stack = []
    for i in range(4):
        if 0 <= y + dy[i] < N and 0 <= x + dx[i] < N and checked[y + dy[i]][x + dx[i]] == 0:
            stack.append((y + dy[i], x + dx[i]))

    return stack

def maze_solver_recur(board, checked, start, end):
    global boolean

    if boolean == True:
        return

    checked[start[0]][start[1]] = 1
    if start == end:
        boolean = True
        return

    else:
        for y, x in find_route(start, checked):
            maze_solver_recur(board, checked, (y, x), end)

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
    boolean = False

    maze_solver_recur(board, checked, start, end)
    if boolean:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))