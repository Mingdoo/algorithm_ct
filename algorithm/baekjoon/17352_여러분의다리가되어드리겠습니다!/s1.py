import sys
N = int(input())

bridges = []

for i in range(N-2):
    bridges.append(list(map(int, sys.stdin.readline().split())))

linked = [[] for _ in range(N + 1)]
for bridge in bridges:
    linked[bridge[0]].append(bridge[1])
    linked[bridge[1]].append(bridge[0])

visited = [0] * (N + 1)

res = []
for i in range(1, N+1):
    if visited[i] == 0:
        stack = [i]
        res.append(i)
        if len(res) >= 2:
            print(res[0], res[1])
            break
        while stack:
            v = stack.pop()
            for land in linked[v]:
                if visited[land] == 0:
                    visited[land] = 1
                    stack.append(land)