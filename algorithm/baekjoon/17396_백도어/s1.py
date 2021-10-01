import sys
import heapq
inf = sys.maxsize
sys.stdin = open('input.txt')
N, M = map(int, sys.stdin.readline().split())

vision = list(map(int, sys.stdin.readline().split()))
vision[-1] = 0
routes = [[] for _ in range(N)]

for i in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    routes[start].append([end, time])
    routes[end].append([start, time])

visited = [inf] * N

q = []
visited[0] = 0
heapq.heappush(q, [0, 0])
while q:
    visit_time, node = heapq.heappop(q)
    if visited[node] < visit_time:
        continue
    else:
        for route in routes[node]:
            num, time = route[0], route[1]
            num_time = visit_time + time
            if visited[num] > num_time and vision[num] == 0:
                visited[num] = num_time
                heapq.heappush(q, [num_time, num])

print(visited[-1] if visited[-1] < inf else -1)