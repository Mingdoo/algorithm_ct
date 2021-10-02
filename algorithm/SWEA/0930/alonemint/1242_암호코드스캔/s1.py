import sys
sys.stdin = open('sample_input.txt')

patterns = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = list(set(input() for _ in range(N)))
    passwords = []

    for i in range(len(board)):
        tmp = []
        for j in range(len(board[i])):
            binary = format(int(board[i][j], 16), 'b')
            four_digit_binary = '0' * (4 - len(binary)) + binary
            tmp.append(four_digit_binary)
        board[i] = ''.join(tmp)
    num = []
    for i in range(len(board)):
        A = B = C = 0
        for j in range(len(board[i])):
            if B == 0 and C == 0 and board[i][j] == '1':
                A += 1
            elif A > 0 and C == 0 and board[i][j] == '0':
                B += 1
            elif A > 0 and B > 0 and board[i][j] == '1':
                C += 1
            elif A > 0 and B > 0 and C > 0 and board[i][j] == '0':
                A, B, C = A // min(A, B, C), B // min(A, B, C), C // min(A, B, C)
                pattern = str(A)+str(B)+str(C)
                num.append(str(patterns[pattern]))
                A = B = C = 0

    code_sum = []
    my_set = set()
    for i in range(len(num)//8):
        my_set.add(''.join(num[8*i: 8*i+8]))

    for code in my_set:
        result = 0
        for j in range(len(code)):
            if j % 2 == 0:
                result += 3 * int(code[j])
            else:
                result += int(code[j])
        if result % 10 == 0 and result > 0:
            s = 0
            for k in range(len(code)):
                s += int(code[k])
            code_sum.append(s)

    print(f'#{tc} {sum(code_sum)}')