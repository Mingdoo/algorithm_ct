import sys
sys.stdin = open('input.txt')

def dfs(v, cost):
    global answer
    if cost >= answer:
        return
    if v == N:
        if cost < answer:
            answer = cost
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                dfs(v+1, cost + board[v][i])
                visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 1e9
    dfs(0, 0)
    print(f'#{tc} {answer}')