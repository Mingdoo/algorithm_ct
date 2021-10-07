def diagonal_check(queens, new_row, queen_no):
    '''
    :param queens: array of queens
    :param new_row: new row
    :param queen_no: number of queen
    :return: boolean value whether new row and queen number can be in queens' array
    '''
    #새로 들어갈 row, queen 번호와 기존의 번호의 기울기를 검사
    for r, c in enumerate(queens):
        #기울기가 1 또는 -1일 경우는 넣을 수 없음.
        if abs((r-new_row) / (c-queen_no)) == 1:
            return False
    return True

def dfs(queens, row):
    '''
    :param queens: array of queens
    :param row: row what we want to put in
    :return: None
    '''
    global answer
    if len(queens) == N:
        answer += 1
    for i in range(N):
        #dfs
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