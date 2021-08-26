import sys
sys.stdin = open('sample_input.txt')

def bfs(start, goal):

    dist = [0] * (V + 1)
    queue = [start]
    checked[start] = 1

    while queue:
        v = queue.pop(0)

        for i in adj_list[v]:
            if checked[i] == 0:
                queue.append(i)
                checked[i] = 1
                dist[i] += dist[v] + 1

    if not checked[goal]:
        return 0
    return dist[goal]



T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]
    checked = [0] * (V + 1)
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(S, G)))
