import sys
sys.stdin = open('input.txt')

#memoization
def find_min(idx):
    global partial_sum, total, tmp

    #제일 중요한 부분. pruning(가지치기)
    if tmp > total:
        return

    #종료조건
    if idx == N:
        if tmp < total:
            total = tmp
    for i in range(N):
        if checked[i] == 0:
            #체크 하고
            checked[i] = 1
            #더하고
            tmp += board[idx][i]
            #탐색
            find_min(idx + 1)

            #체크 취소하고
            checked[i] = 0
            #다시 탐색
            tmp -= board[idx][i]

    return total

T = int(input())

for tc in range(1, T + 1):

    #init block
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    checked = [0] * N

    tmp = 0
    idx = 0
    total = 2 ** 64

    print('#{} {}'.format(tc, find_min(0)))