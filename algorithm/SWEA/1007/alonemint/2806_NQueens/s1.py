def diagonal_check(queens, new_row, queen_no):
    for r, c in enumerate(queens):
        if abs((r-new_row) / (c-queen_no)) == 1:
            return False
    return True

def dfs(queens, row):
    global answer
    if len(queens) == N:
        answer += 1
    for i in range(N):
        if visited[i] == 0 and diagonal_check(queens, row, i):
            visited[i] = 1
            queens.append(i)
            dfs(queens, row+1)
            queens.remove(i)
            visited[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    queens = []
    visited = [0] * N
    answer = 0
    dfs(queens, 0)
    print(f'#{tc} {answer}')