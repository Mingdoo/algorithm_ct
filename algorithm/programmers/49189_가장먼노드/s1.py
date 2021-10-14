from collections import deque

def solution(n, edge):
    linked = [[] for _ in range(n+1)]
    for link in edge:
        linked[link[0]].append(link[1])
        linked[link[1]].append(link[0])

    visited = [0] * (n+1)
    q = deque([1])
    visited[1] = 1
    while q:
        v = q.popleft()
        for node in linked[v]:
            if visited[node] == 0:
                visited[node] = visited[v] + 1
                q.append(node)

    return visited.count(max(visited))

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))