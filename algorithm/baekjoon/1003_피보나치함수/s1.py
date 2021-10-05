fib = [0] * 41
fib_cnt = [[] for _ in range(41)]

fib[0] = 0
fib[1] = 1

fib_cnt[0] = [1, 0]
fib_cnt[1] = [0, 1]

for i in range(2, 41):
    fib[i] = fib[i-1] + fib[i-2]
    fib_cnt[i].append(fib_cnt[i-1][0] + fib_cnt[i-2][0])
    fib_cnt[i].append(fib_cnt[i-1][1] + fib_cnt[i-2][1])

N = int(input())
for _ in range(N):
    n = int(input())
    print(*fib_cnt[n])
