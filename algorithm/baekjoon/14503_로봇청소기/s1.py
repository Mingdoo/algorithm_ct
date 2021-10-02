#0 1 2 3
#북 동 남 서
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
status =list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]

Y = status[0]
X = status[1]
direction = status[2]

def find_cor(Y, X, direction, board):
    if direction == 1:
        if X < len(board[0]) - 1:
            return (Y, X+1)
        else:
            return (Y, X)
    elif direction == 2:
        if Y < len(board) - 1:
            return (Y+1, X)
        else:
            return (Y, X)    
    elif direction == 3:
        if X > 0:
            return (Y, X-1)
        else:
            return (Y, X)
    else:
        if Y > 0:
            return (Y-1, X)
        else:
            return (Y, X)
while True:
    flag = False
    for i in range(4):
        if board[find_cor(X,Y,i,board)[0]][find_cor(X,Y,i,board)[1]] == 0:
            flag = True
    if flag == False:
        break

    if direction == 1:
        

    

