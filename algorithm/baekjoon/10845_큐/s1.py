import sys

class Queue:
    def __init__(self):
        self.q = []

    def push(self, number):
        self.q.append(number)

    def pop(self):
        if not self.empty():
            return self.q.pop(0)
        else:
            return -1
    def empty(self):
        if self.q:
            return 0
        else:
            return 1
    def back(self):
        if self.q:
            return self.q[-1]
        else:
            return -1

    def front(self):
        if self.q:
            return self.q[0]
        else:
            return -1

    def size(self):
        return len(self.q)

q = Queue()
N = int(input())
for _ in range(N):
    order = list(sys.stdin.readline().split())
    if order[0] == 'push':
        q.push(int(order[1]))
    elif order[0] == 'back':
        print(q.back())
    elif order[0] == 'size':
        print(q.size())
    elif order[0] == 'pop':
        print(q.pop())
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'front':
        print(q.front())