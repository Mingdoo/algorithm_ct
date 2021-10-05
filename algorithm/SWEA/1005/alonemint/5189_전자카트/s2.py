import sys
sys.stdin = open('sample_input.txt')

from itertools import permutations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    p = [_ for _ in range(1, N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    perm = list(permutations(p, N-1))
    print(perm)
    answer = 987654321

    for element in perm:
        res = 0
        res += board[0][element[0]]

        for i in range(len(element) - 1):
            frm = element[i]
            to = element[i + 1]
            res += board[frm][to]

        res += board[element[len(element) - 1]][0]
        if res < answer:
            answer = res
    print(f'#{tc} {answer}')