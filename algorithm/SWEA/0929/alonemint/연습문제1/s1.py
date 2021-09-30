import sys
sys.stdin = open('input.txt')

num = input()
for i in range(len(num)//7):
    print(int(num[7*i:7*i+7], 2))