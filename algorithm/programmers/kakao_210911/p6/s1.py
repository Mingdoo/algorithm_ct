def solution(board, skill):
    cnt = 0

    for sk in skill:

        type = sk[0]

        r1 = sk[1]
        c1 = sk[2]

        r2 = sk[3]
        c2 = sk[4]
        degree = sk[5]

        #attacked

        if type == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= degree
        elif type == 2:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += degree
    for i in range(len(board)):
        for j in range(len(board[1])):
            if board[i][j] >= 1:
                cnt += 1

    return cnt

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))