import sys
input = sys.stdin.readline
n = input()
N = set(input().split())
m = input()
M = input().split()

for l in M:
    if l in N:
        print(1)
    else:
        print(0)