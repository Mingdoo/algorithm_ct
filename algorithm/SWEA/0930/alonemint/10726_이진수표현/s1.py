import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = 'ON'
    for i in range(N):
        if not M & (1 << i):
            res = 'OFF'
            break
    print(f'#{tc} {res}')