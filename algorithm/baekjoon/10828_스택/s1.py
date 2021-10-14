import sys

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, number):
        self.stack.append(number)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return -1
    def empty(self):
        if self.stack:
            return 0
        else:
            return 1
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def size(self):
        return len(self.stack)

s = Stack()
N = int(input())
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        s.push(int(order[1]))
    elif order[0] == 'top':
        print(s.top())
    elif order[0] == 'size':
        print(s.size())
    elif order[0] == 'pop':
        print(s.pop())
    elif order[0] == 'empty':
        print(s.empty())