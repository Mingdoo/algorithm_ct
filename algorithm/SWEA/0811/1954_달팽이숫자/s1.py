import sys
sys.stdin = open('input.txt')

#define current status
def status(Arr, i, j, state):
    if state == 'right':
        if (j == len(Arr) - 1):
            return 'down'
        elif Arr[i][j + 1] != 0:
            return 'down'
        else:
            return 'right'
    if state == 'left':
        if i == 0:
            return 'up'
        elif Arr[i][j - 1] != 0:
            return 'up'
        else:
            return 'left'
    if state == 'down':
        if i == len(Arr) - 1:
            return 'left'
        elif Arr[i + 1][j] != 0:
            return 'left'
        else:
            return 'down'
    if state == 'up':
        if Arr[i - 1][j] != 0:
            return 'right'
        else:
            return 'up'

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())


    #initialization block
    board = [[0 for x in range(N)] for y in range(N)]
    number = 1
    i = j = 0
    state = 'right'
    board[0][0] = number
    number += 1

    #algorithm
    while (number <= N ** 2):

        #re-define status everytime
        if state == 'right':
            j += 1
            board[i][j] = number
            number += 1
            state = status(board, i, j, state)
        elif state == 'left':
            j -= 1
            board[i][j] = number
            number += 1
            state = status(board, i, j, state)

        elif state == 'down':
            i += 1
            board[i][j] = number
            number += 1
            state = status(board, i, j, state)

        else:
            i -= 1
            board[i][j] = number
            number += 1
            state = status(board, i, j, state)
    print('#{}'.format(test_case))

    #printing block
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()