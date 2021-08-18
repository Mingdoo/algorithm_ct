import sys
sys.stdin = open('test_input.txt', encoding = 'UTF-8')

# T = int(input())
T = 10
for test_case in range(1, T + 1):

    N = input()
    my_chars = input()

    txt = list(input().split(my_chars))

    print('#{} {}'.format(test_case, len(txt) - 1))