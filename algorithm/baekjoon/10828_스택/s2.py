import sys
from collections import deque
N = int(input())
s = deque()
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        s.append(int(order[1]))
    elif order[0] == 'top':
        if s:
            print(s[-1])
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(s))
    elif order[0] == 'pop':
        if s:
            print(s.pop())
        else:
            print(-1)
    elif order[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)