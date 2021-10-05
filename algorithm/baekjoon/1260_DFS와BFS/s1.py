N, M, V = map(int, input().split())

linked = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    linked[a].append(b)
    linked[b].append(a)

for i in range(len(linked)):
    linked[i] = sorted(linked[i])

dfs_visited = [0] * (N+1)
bfs_visited = [0] * (N+1)

def dfs(v):
    if dfs_visited[v] == 0:
        dfs_visited[v] = 1
        print(v, end=' ')
    for node in linked[v]:
        if dfs_visited[node] == 0:
            dfs(node)

def bfs(v):
    q = [v]
    bfs_visited[v] = 1
    while q:
        p = q.pop(0)
        print(p, end=' ')
        for node in linked[p]:
            if bfs_visited[node] == 0:
                bfs_visited[node] = 1
                q.append(node)
dfs(V)
print()
bfs(V)
