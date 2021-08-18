import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]

    #우하좌상 순서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    total = 0
    for i in range(size):
        for j in range(size):
            for mode in range(4):

                R_idx = i + dy[mode]
                C_idx = j + dx[mode]

                if 0 <= R_idx < size and 0 <= C_idx < size:
                    total += abs(board[R_idx][C_idx] - board[i][j])

    print('#{} {}'.format(test_case, total))