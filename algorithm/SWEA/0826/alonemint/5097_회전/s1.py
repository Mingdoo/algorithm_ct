import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    i = 0

    while i < M:
        v = arr.pop(0)
        arr.append(v)
        i += 1

    print('#{} {}'.format(tc, arr[0]))