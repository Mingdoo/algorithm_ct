import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):

    A, B = input().split()
    A = A.replace(B, chr(11231))
    print('#{} {}'.format(test_case, len(A)))