import sys
sys.stdin = open('input2.txt')

def dfs(picked, idx, steps):
    global answer
    if idx == 4:
        tmp = (board[steps[0]]+ board[steps[3]])**2 + (board[steps[1]] + board[steps[2]])**2
        tmp2 = (board[steps[0]]+ board[steps[1]])**2 + (board[steps[2]] + board[steps[3]])**2
        tmp_ans = max(tmp, tmp2)
        if tmp_ans > answer:
            answer = tmp
        return
    else:
        for i in range(picked+2, N):
            visited[i] = 1
            dfs(i, idx+1, steps + [i])
            visited[i] = 0
for tc in range(1, int(input())+1):
    N = int(input())
    board = list(map(int, input().split()))
    choices = [n for n in range(N)]
    answer = 0
    for j in range(N - 6):
        arr = []
        visited = [0] * N
        dfs(j, 1, [j])
    print('#{} {}'.format(tc, answer))