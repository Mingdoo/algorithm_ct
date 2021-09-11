minimum = 987654321
bd = []
def dfs(n, apeach, board, idx=10):
    global minimum
    global bd
    if n < 0:
        return

    elif n == 0 or idx == 0:

        if apeach <= minimum:
            minimum = apeach
            bd = board[:]
        return

    if board[idx] > 1 and n - board[idx] >= 0:
        dfs(n - board[idx], apeach - 2 *(10 - idx), board=board[:idx] + [999] + board[idx+1:], idx = idx - 1)
        dfs(n, apeach, board, idx - 1)
    else:
        if n - board[idx] >= 0:
            dfs(n - board[idx], apeach - (10 - idx), board=board[:idx] + [999] + board[idx + 1:], idx=idx - 1)
        dfs(n, apeach, board, idx - 1)

def solution(n, info):
    answer = [[] for _ in range(len(info))]
    board = [[] for _ in range(len(info))]
    for i in range(len(info)):
        board[i] = info[i] + 1

    apeach = 0
    for i in range(len(info)):
        if info[i] != 0:
            apeach += (10 - i)

    dfs(n, apeach, board)
    for i in range(len(bd)):
        if bd[i] < 999:
            answer[i] = 0
        else:
            answer[i] = board[i]

    if minimum >= 0:
        return [-1]
    if sum(answer) < n:
        answer[-1] = n - sum(answer)

    return answer

# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]
# print(solution(n, info))
# print("expect = [0,2,2,0,1,0,0,0,0,0,0]")
#
# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# print(solution(n, info))
# print("expect = [-1]")
#
# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]
# print(solution(n, info))
# print("expect = [1,1,2,0,1,2,2,0,0,0,0]")
#
# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]
# print(solution(n, info))
# print("expect = [1,1,1,1,1,1,1,1,0,0,2]")

n = 2
info = [0,1,0,0,0,0,0,0,0,0,1]
print(solution(n, info))