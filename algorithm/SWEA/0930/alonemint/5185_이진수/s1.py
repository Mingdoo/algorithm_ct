import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    _, num = list(input().split())
    num = list(num)
    for i in range(len(num)):
        binary = format(int(num[i], 16), 'b')
        num[i] = '0' * (4 - len(binary)) + binary

    num = ''.join(num)
    print(f'#{tc} {num}')