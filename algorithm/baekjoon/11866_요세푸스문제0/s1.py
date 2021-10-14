from collections import deque

N, K = map(int, input().split())
q = deque([n for n in range(1, N+1)])
cnt = 0
result = []
while q:
    v = q.popleft()
    cnt += 1
    if cnt % K == 0:
        result.append(v)
    else:
        q.append(v)
print('<', end='')
print(*result, sep=', ', end='')
print('>')