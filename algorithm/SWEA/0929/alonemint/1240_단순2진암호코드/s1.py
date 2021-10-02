import sys

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]

    passwords = []
    for row in board:
        for j in range(len(row)-1, 0, -1):
            if row[j] == '1':
                passwords.append(row[j-55:j+1])
                break
    numbers = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    bool = True
    for password in passwords:
        decrypted = []
        for i in range(len(password) // 7):
            decrypted.append(numbers[password[7 * i:7 * i + 7]])
        res = 0
        for i in range(len(decrypted)):
            if i % 2 == 0:
                res += 3 * decrypted[i]
            else:
                res += decrypted[i]
        if res % 10 == 0 and res > 0:
            print(f'#{tc} {sum(decrypted)}')
            bool = True
            break
        bool = False
    if bool == False:
        print(f'#{tc} 0')