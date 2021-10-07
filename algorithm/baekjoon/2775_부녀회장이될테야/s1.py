from pprint import pprint
numbers = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],]

#층
for i in range(1, 15):
    tmp = []
    for j in range(0, 15):
        tmp.append(sum(numbers[i-1][1:j+1]))
    numbers.append(tmp)

T = int(input())
for test_case in range(T):
    k = int(input())
    n = int(input())
    print(numbers[k][n])
