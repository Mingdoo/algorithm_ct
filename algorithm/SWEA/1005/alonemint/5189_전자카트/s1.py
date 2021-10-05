import sys
sys.stdin = open('sample_input.txt')

def dfs(v):
    if len(result) == N - 1:
        ans = 0
        for i, j in result:
            ans += board[i][j]
        ans += board[j][0]
        answer.append(ans)
        return

    for i in range(1, N):
        if not visited[i]:
            result.append([v, i])
            visited[i] = 1
            dfs(i)
            result.remove([v, i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = []
    result = []
    visited = [0] * N
    dfs(0)
    print(f'#{tc} {min(answer)}')
