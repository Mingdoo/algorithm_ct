import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(v, prob):
    print(visited)
    global max_prob
    if v == N and prob > max_prob:
        max_prob = prob
        return

    if prob <= max_prob:
        return
    else:

        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(v + 1, prob * probabilities[v][i])
                visited[i] = 0


for tc in range(1, T+1):
    N = int(input())
    probabilities = [list(map(lambda a: int(a)/100, input().split())) for _ in range(N)]

    max_prob = 0
    visited = [0] * N
    dfs(0, 1)
    print(f'#{tc} {max_prob * 100:.6f}')
