import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    num = int(input())

    arr = list(map(int, input().split()))
    res = []

    #bubble sort 응용
    for i in range(10):
        for j in range(len(arr)-1, i, -1):
            #even case
            if not i % 2:
                if arr[j] > arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
            #odd case
            else:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]

    print('#{}'.format(test_case), end = ' ')
    for number in arr[:10]:
        print(number, end = ' ')
    print()
