import sys
N, M = map(int, sys.stdin.readline().split())
table = {}
for i in range(N):
    name = input()
    table[name] = table.get(name, 0) + 1

res = []
for j in range(M):
    name = input()
    if table.get(name, False):
        res.append(name)

print(len(res))
res.sort()
for e in res:
    print(e)