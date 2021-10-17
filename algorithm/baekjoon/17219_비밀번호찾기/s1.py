N, M = map(int, input().split())
t = {}
for _ in range(N):
    i, j = input().split()
    t[i] = t.get(i, j)
for _ in range(M):
    i = input()
    print(t[i])//                     