import sys
sys.stdin = open('input.txt')

N = int(input())
switches = list(map(int, input().split()))

number = int(input())

for _ in range(number):
    gender, switch = map(int, input().split())

    #남자
    if gender == 1:
        i = 0
        while (i + 1) * switch - 1 < len(switches):
            switches[(i + 1) * switch - 1] = -(switches[(i + 1) * switch - 1]) + 1
            i += 1
    else:
        i = 1

        while switches[switch - 1 - i: switch + i] == switches[switch - 1 - i: switch + i][::-1] and switch - 1 - i >= 0 and switch - 1 + i < len(switches):
            i += 1

        for j in range(switch - i, switch + i - 1):
            switches[j] = -(switches[j]) + 1

for J in range(0, N, 20):
    print(*switches[J: J+20])