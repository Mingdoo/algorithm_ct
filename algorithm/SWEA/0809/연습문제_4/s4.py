import sys
sys.stdin = open('input.txt')

repeat = int(input())

for i in range(repeat):
    num = int(input())
    c = [0] * 12
    for _ in range(6):
        c[num % 10] += 1
        num //= 10

    i = 0
    tri = run = 0

    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri += 1
            continue

        while c[i] >= 0 or (c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1):
            if c[i] == 0:
                i += 1
                break
            elif c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
                c[i] -= 1
                c[i+1] -= 1
                c[i+2] -= 1
                run += 1
                continue
            else:
                i += 1
                break
    if run + tri == 2:
        print("Baby Gin")
    else:
        print("Lose")