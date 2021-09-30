import sys
sys.stdin = open('input.txt')

num = list(input())
for i in range(len(num)):
    binary = format(int(num[i], 16), 'b')
    num[i] = '0' * (4 - len(binary)) + binary

num = ''.join(num)
print(num)
for i in range(len(num)//7+1):
    print(int(num[7*i:7*i+7], 2))