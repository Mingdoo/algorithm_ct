from collections import deque

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    linked = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for i in range(M):
        linked[lst[2 * i]].append(lst[2 * i + 1])
        linked[lst[2 * i + 1]].append(lst[2 * i])

    answer = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            answer += 1
            q = deque([i])
            while q:
                v = q.pop()
                for node in linked[v]:
                    if visited[node] == 0:
                        visited[node] = 1
                        q.append(node)
    print(f'#{tc} {answer}')