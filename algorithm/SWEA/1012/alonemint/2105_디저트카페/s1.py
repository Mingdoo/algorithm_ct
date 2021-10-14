import sys
sys.stdin = open('sample_input.txt')

def dfs(r, c, passed, direction):
    global answer
    tmp_direction = direction
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and board[nr][nc] not in passed and visited[nr][nc] == 0:
            if direction <= i <= direction + 1:
                direction_visited[i] = 1
                passed.append(board[nr][nc])
                visited[nr][nc] = 1
                direction = i
                dfs(nr, nc, passed, direction)
                visited[nr][nc] = 0
                direction = tmp_direction
                passed.remove(board[nr][nc])

        if sum(direction_visited) >= 3 and [nr, nc] == start:
            ans = len(passed)
            answer = max(ans, answer)

#시계
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = -1
    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            direction_visited = [0] * 4
            start = [i, j]
            dfs(i, j, [board[i][j]], -1)

    print(f'#{tc} {answer}')