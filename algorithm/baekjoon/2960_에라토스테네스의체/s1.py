import sys

N, K = map(int, input().split())

arr = [_ for _ in range(0,N+1)]
cnt = 0
for i in range(2, N+1):
    if arr[i] != 0:
        arr[i] = 0
        cnt += 1
        if cnt == K:
            print(i)
        idx = 0
        while i * (idx + 1) <= N:
            if arr[i * (idx + 1)] != 0:
                arr[i * (idx + 1)] = 0
                cnt += 1
                if cnt == K:
                    print(i * (idx + 1))
            idx += 1
