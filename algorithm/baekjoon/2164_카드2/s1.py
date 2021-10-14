from collections import deque
N = int(input())
stack = deque([n for n in range(N, 0, -1)])
while len(stack) >= 2:
    stack.pop()
    stack.appendleft(stack.pop())

print(stack[0])