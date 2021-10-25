# 3단계
def dfs(idx, total):
    global answer
    if total >= answer:
        return

    if idx == N-1:
        if total < answer:
            answer = total
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                dfs(idx+1, total + tmp_board[idx][j])
                visited[j] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 1e9

    for i in range(N):
        tmp_board = board[:i] + board[i+1:]
        for j in range(N):
            visited[j] = 1
            for k in range(N):
                if visited[k] == 0:
                    visited[k] = 1
                    dfs(1, tmp_board[0][k])
                    visited[k] = 0
            visited[j] = 0
    print(f'#{tc} {answer}')