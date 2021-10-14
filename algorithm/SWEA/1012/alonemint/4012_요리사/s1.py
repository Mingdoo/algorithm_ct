import sys
sys.stdin = open('sample_input.txt')

from itertools import combinations
def total(items):
    result = 0
    for a, b in list(combinations(items, 2)):
        result += sng[a][b] + sng[b][a]
    return result

def dfs(idx, where):
    global answer
    if idx == N // 2:
        A = []
        B = []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        result = abs(total(A) - total(B))
        answer = min(result, answer)
        return

    for i in range(where, N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx+1, i+1)
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    sng = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e9
    visited = [0] * N
    dfs(0, 0)
    print(f'#{tc} {answer}')
