import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    Q_num = int(input())

    matrix = [list(map(int, input().split())) for _ in range(100)]
    total_list = []

    #rowwise
    for row in matrix:
        total_list.append(sum(row))

    #columnwise
    for j in range(100):
        row_total = 0
        for i in range(100):
            row_total += matrix[i][j]
        total_list.append(row_total)

    #diagonalwise
    diagonal_total1 = 0
    diagonal_total2 = 0
    for i in range(100):
        diagonal_total1 += matrix[i][i]
        diagonal_total2 += matrix[i][99 - i]

    total_list.append(diagonal_total1)
    total_list.append(diagonal_total2)

    print('#{} {}'.format(Q_num, max(total_list)))