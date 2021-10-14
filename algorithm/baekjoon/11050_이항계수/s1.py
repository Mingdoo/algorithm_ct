def fac(n):
    if n == 0:
        return 1
    if n <= 2:
        return n
    else:
        return n*fac(n-1)

N, K = map(int, input().split())
print(fac(N) // (fac(N-K) * fac(K)))