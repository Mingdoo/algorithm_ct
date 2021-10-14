import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    INF = 1e9
    visited = [0] * (V + 1)
    cost = [INF] * (V + 1)
    path = [-1] * (V + 1)
    linked = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        linked[n1].append([n2, w])

    start = 0
    visited[start] = 1
    cost[start] = 0
    for node, w in linked[start]:
        cost[node] = w
        path[node] = start

    while sum(visited) <= V:
        m = INF
        idx = -1
        for i in range(V + 1):
            if not visited[i] and cost[i] < m:
                idx = i
                m = cost[i]
        visited[idx] = 1
        for node, w in linked[idx]:
            if cost[node] > w + cost[idx] and not visited[node]:
                cost[node] = w + cost[idx]
                path[node] = idx

    print(f'#{tc} {cost[-1]}')



