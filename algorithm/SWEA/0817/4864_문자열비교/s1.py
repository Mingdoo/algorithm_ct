import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    target = input()
    #파이썬 개사기
    text = input().split(target)

    boolean = 0
    if len(text) >= 2:
        boolean = 1

    print('#{} {}'.format(test_case, boolean))
