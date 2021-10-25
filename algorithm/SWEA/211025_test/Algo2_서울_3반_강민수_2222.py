# 2단계

def dfs(idx, total, steps):
    global answer
    if total >= answer:
        return

    if idx == N:
        if total < answer:
            answer = total
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(idx+1, total + board[idx][j], steps + [j])
                visited[j] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 1e9

    for i in range(N):
        visited[i] = 1
        dfs(1, board[0][i], [i])
        visited[i] = 0
    print(f'#{tc} {answer}')