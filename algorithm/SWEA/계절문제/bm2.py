#방문한 곳을 다시 방문하지 않을 때

import time

def dfs2(v):
    global ans
    if v >= N:
        visited[N] = 0
        if visited.count(2) == visited.count(1):
            ans += 1
    else:
        for i in range(1, 7):
            if v + i <= N and visited[v + i] == 0:
                visited[v + i] = 2
                dfs2(v + i)
                visited[v + i] = 0

def dfs(v):
    if v >= N:
        visited[N] = 0
        dfs2(0)
    else:
        for i in range(1, 7):
            if v + i <= N and visited[v + i] == 0:
                visited[v + i] = 1
                dfs(v + i)
                visited[v + i] = 0

a = time.time()
N = 10
visited = [0] * (N + 1)
ans = 0
dfs(0)
print(ans, time.time() - a)