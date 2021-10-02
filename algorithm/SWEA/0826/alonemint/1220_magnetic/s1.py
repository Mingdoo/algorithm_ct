import sys
sys.stdin = open('input.txt')

def transpose(arr):
    arr2 = []

    for row in range(len(arr)):
        tmp = ''
        for col in range(len(arr)):
            tmp += arr[col][row]
        arr2.append(tmp)
    return arr2

T = 10

for tc in range(1, T + 1):

    size = int(input())
    board = [input().split() for _ in range(size)]
    new_board = transpose(board)

    cnt = 0
    for i in range(size):
        new_board[i] = new_board[i].replace('0', '')
        cnt += new_board[i].count('12')

    print('#{} {}'.format(tc, cnt))
