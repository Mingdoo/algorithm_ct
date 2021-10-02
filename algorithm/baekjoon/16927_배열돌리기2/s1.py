import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline
def rotate(left_top, right_bottom, board):
    #윗라인을 왼쪽으로 이동
    l_r = left_top[0]
    l_c = left_top[1]

    r_r = right_bottom[0]
    r_c = right_bottom[1]
    tmp = board[l_r][l_c]
    for i in range(l_c + 1, r_c + 1):
        board[l_r][i-1] = board[l_r][i]

    for i in range(l_r + 1, r_r + 1):
        board[i-1][r_c] = board[i][r_c]

    for i in range(r_c - 1, l_c - 1, -1):
        board[r_r][i+1] = board[r_r][i]

    for i in range(r_r - 1, l_r - 1, -1):
        board[i+1][l_c] = board[i][l_c]

    board[l_r+1][l_c] = tmp
    return board

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

start, end = [0,0], [N-1, M-1]
rotate_list = [[start, end]]
element_counter = [4 + 2*(N-2) + 2*(M-2)]
while end[0] - start[0] > 2 and end[1] - start[1] > 2:
    start = [start[0] + 1, start[1] + 1]
    end = [end[0] - 1, end[1] - 1]
    rotate_list.append([start, end])
    element_counter.append(4 + 2*(end[1]-start[1]-1) + 2*(end[0]-start[1]-1))

for i in range(len(rotate_list)):
    for j in range(R % element_counter[i]):
        board = rotate(rotate_list[i][0], rotate_list[i][1], board)

for row in board:
    print(*row, sep=' ')