import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    numbers = list(map(int, input().split()))
    arr = [[]]


    for number in numbers:
        tmp = arr[:]
        for elem in tmp:
            arr.append(elem + [number])


    boolean = 0
    for subset in arr:
        if sum(subset) == 0 and len(subset) != 0:
            boolean = 1
            break

    print('#{} {}'.format(test_case, boolean))

