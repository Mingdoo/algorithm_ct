def dfs(v, steps):
    '''
    :param v: 현재 위치
    :param steps: 지금까지 진행한 경로
    :return: None
    '''
    global answer, answer2
    #answer2는 경로 개수를 의미한다.
    if v == end:
        answer = 1
        answer2 += 1
        return

    r = v[0]
    c = v[1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        #1. 범위 안에 들어오는가
        #2. 갈 수 있는 길인가(통로, 출발, 도착)
        #3. 진행해온 경로에 있는가(없으면 다음단계로)
        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and board[nr][nc] in '023' and [nr, nc] not in steps:
            #1. 방문 체크
            visited[nr][nc] = 1
            #2. 다음 스텝의 dfs
            dfs([nr, nc], steps + [[nr, nc]])
            #3. 방문 취소
            visited[nr][nc] = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for tc in range(1, int(input())+1):
    #init block
    N = int(input())
    board = [list(input().split()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '2':
                start = [i, j]
            elif board[i][j] == '3':
                end = [i, j]
    visited = [[0] * N for _ in range(N)]

    #answer block
    answer = 0
    answer2 = 0

    #function call block
    dfs(start, [start])

    if not answer:
        print('#{} {}'.format(tc, answer))
    else:
        print('#{} {} {}'.format(tc, answer, answer2))