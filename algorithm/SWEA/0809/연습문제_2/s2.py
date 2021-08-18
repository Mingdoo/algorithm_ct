import sys
sys.stdin = open('input.txt')

rnum, cnum = map(int,input().split())

matrix = []
for i in range(rnum):
    sum = 0
    inp = list(map(int, input().split()))
    for j in range(cnum):
        sum += inp[j]
    print(sum)