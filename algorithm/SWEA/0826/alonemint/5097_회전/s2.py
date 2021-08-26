import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    #front와 rear를 통한 구현
    front = 0
    rear = len(arr) - 1

    i = 0
    while i < M:
        v = arr[front]
        front += 1
        arr.append(v)
        rear += 1
        i += 1

    print('#{} {}'.format(tc, arr[front]))