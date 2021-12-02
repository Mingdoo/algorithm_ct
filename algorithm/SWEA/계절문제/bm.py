#방문한 곳을 다시 방문할 때

import time
from collections import defaultdict

def dfs(v):
    if v >= N:
        visited[N] = 0
        my_dict[sum(visited)] += 1
    else:
        for i in range(1, 7):
            if v + i <= N and visited[v + i] == 0:
                visited[v + i] = 1
                dfs(v + i)
                visited[v + i] = 0

a = time.time()
N = 20
visited = [0] * (N + 1)
my_dict = defaultdict(int)
ans = 0
dfs(0)
for val in my_dict.values():
    ans += val ** 2
    ans = ans % 100000007
print(ans, time.time() - a)