import sys
sys.stdin = open('GNS_test_input.txt', encoding = 'UTF-8')

T = int(input())

str_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for test_case in range(1, 1 + T):

    number = list(map(str, input().split()))
    my_list = list(map(str, input().split()))
    res = [0 for _ in range(10)]
    for elem in my_list:
        res[str_num.index(elem)] += 1

    print(number[0])
    for iter in range(10):
        print('{} '.format(str_num[iter]) * res[iter])