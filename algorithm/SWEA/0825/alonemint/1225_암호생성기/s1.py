import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):

    N = int(input())

    passwords = list(map(int, input().split()))

    i = 0
    while passwords[-1] != 0:
        q = passwords.pop(0)
        if q > 0:
            q -= (i % 5) + 1
            # print((i % 5) + 1)
            passwords.append(max(0, q))
        i += 1

    print('#{}'.format(tc), end= ' ')
    print(*passwords, sep = ' ')