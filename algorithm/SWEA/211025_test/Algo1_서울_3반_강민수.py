for tc in range(1, 1 + int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = [[0] * (2*N) for _ in range(2*N)]

    for i in range(2*N):
        for j in range(2*N):
            if i < N and j < N:
                answer[i][j] = board[i][j]
            elif i >= N and j < N:
                answer[i][j] = board[N-i-1][j]
            elif i < N and j >= N:
                answer[i][j] = board[i][N-j-1]
            else:
                answer[i][j] = board[N-j-1][N-i-1]

    print(f'#{tc}')
    for row in answer:
        print(*row)