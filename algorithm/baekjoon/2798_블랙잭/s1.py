from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
combs = list(combinations(lst, 3))
for i in range(len(combs)):
    combs[i] = M - sum(combs[i]) if M - sum(combs[i]) >= 0 else float('INF')

combs.sort()
print(M - combs[0])