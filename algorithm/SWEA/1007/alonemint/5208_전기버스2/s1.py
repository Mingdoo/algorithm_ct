import sys
sys.stdin = open('input.txt')

def dfs(v, charged, visited=0):
    global answer
    if visited >= answer:
        return

    if v >= N-1:
        if visited < answer:
            answer = visited
        return
    else:
        for idx in range(1, charged+1):
            dfs(v+idx, charges[v+idx], visited+1)


for tc in range(1, int(input())+1):
    charges = list(map(int, input().split()))
    N = charges[0]
    charges = charges[1:] + [0] * N
    answer = 100
    dfs(0, charges[0])
    print(f'#{tc} {answer - 1}')