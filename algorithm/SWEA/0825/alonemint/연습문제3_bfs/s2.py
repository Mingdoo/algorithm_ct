import sys
sys.stdin = open('input.txt')

V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))
visited = [0 for _ in range(V+1)]
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = graph_list[2 * i], graph_list[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

def bfs(start, V):
    queue = []
    queue.append(start)

    while queue:
        v = queue.pop(0)
        if visited[v] == 0:
            visited[v] = 1
            print(v, end = ' ')
            print(visited)

        for i in adj_list[v]:
            if visited[i] == 0:
                queue.append(i)

bfs(1, V)