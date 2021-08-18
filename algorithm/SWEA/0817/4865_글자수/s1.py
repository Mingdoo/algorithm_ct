import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    target = input()

    my_dict = {}
    for char in target:
        my_dict[char] = 0

    text = input()
    for char in text:
        if my_dict.get(char) != None:
            my_dict[char] += 1

    print('#{} {}'.format(test_case, max(my_dict.values())))