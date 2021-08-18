import sys

sys.stdin = open('input.txt')

number = int(input())
result = '홀수' if number % 2 else '짝수'
print(result)

numbers = list(map(int,input().split()))

total = 0
for number in numbers:
    total += number

print(total)

N = int(input())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

res = 0
for row in matrix:
    for element in row:
        res += element

print(res)