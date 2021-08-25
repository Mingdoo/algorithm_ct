import sys
sys.stdin = open('input.txt')

from itertools import permutations
T = int(input())

def brute_force(board, permutations):
    minimum = 10000000000

    for i in range(len(permutations)):
        partial_sum = 0
        for j in range(len(permutations[0])):
            partial_sum += board[j][permutations[i][j]]
        if partial_sum < minimum:
            minimum = partial_sum
    return minimum

for tc in range(1, T + 1):

    N = int(input())
    p = [num for num in range(N)]

    board = [list(map(int, input().split())) for _ in range(N)]

    perm = list(permutations(p))

    print('#{} {}'.format(tc, brute_force(board, perm)))