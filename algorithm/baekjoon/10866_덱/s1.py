import sys
from collections import deque
class Queue:
    def __init__(self):
        self.q = deque()

    def push_front(self, number):
        self.q.appendleft(number)

    def push_back(self, number):
        self.q.append(number)

    def pop_front(self):
        if not self.empty():
            return self.q.popleft()
        else:
            return -1

    def pop_back(self):
        if not self.empty():
            return self.q.pop()
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
    if order[0] == 'push_front':
        q.push_front(int(order[1]))
    elif order[0] == 'push_back':
        q.push_back(int(order[1]))
    elif order[0] == 'back':
        print(q.back())
    elif order[0] == 'size':
        print(q.size())
    elif order[0] == 'pop_front':
        print(q.pop_front())
    elif order[0] == 'pop_back':
        print(q.pop_back())
    elif order[0] == 'empty':
        print(q.empty())
    elif order[0] == 'front':
        print(q.front())