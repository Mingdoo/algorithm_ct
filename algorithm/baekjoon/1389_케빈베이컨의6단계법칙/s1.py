N, M = map(int, input().split())
linked = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    linked[a].append(b)
    linked[b].append(a)

for i in range(N):
    linked[i] = sorted(linked[i])

bacon = 987654321
answer = -1
for j in range(1, N+1):
    visited = [1e9] * (N+1)
    stack = [j]
    visited[j] = 0
    while stack:
        v = stack.pop()
        for node in linked[v]:
            if visited[node] > visited[v] + 1:
                visited[node] = visited[v] + 1
                stack.append(node)
    s = sum(visited[1:])
    if bacon > s:
        bacon = s
        answer = j
print(answer)
