import sys
sys.stdin = open('input.txt')

V, E = list(map(int, input().split()))

graph_list = list(map(int, input().split()))
graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for i in range(E):
    n1, n2 = graph_list[2 * i], graph_list[2 * i + 1]
    graph[n1][n2] = 1
    graph[n2][n1] = 1

def bfs(start, V):
    queue = []
    queue.append(start)

    while queue:
        v = queue.pop(0)
        if visited[v] == 0:
            visited[v] = 1
            print(v, end = ' ')

        for i in range(1, V + 1):
            if graph[v][i] == 1 and visited[i] == 0:
                queue.append(i)

bfs(1, V)