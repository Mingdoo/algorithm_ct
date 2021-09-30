import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = float(input())
    res = []
    exponent = -1
    boolean = True
    while num > 0:
        if len(res) >= 13:
            boolean = False
            break
        elif num >= 2**exponent:
            res.append('1')
            num -= 2**exponent
        else:
            res.append('0')
        exponent -= 1

    res = ''.join(res) if boolean == True else 'overflow'
    print(f'#{tc} {res}')
