from collections import deque

def bfs(n):
    q = deque()
    q.append([n, 0])
    visited = set()
    while q:
        num, cnt = q.popleft()
        if num > 1000000 or num < 0:
            continue

        if num in visited:
            continue

        visited.add(num)
        if num == M:
            return cnt

        cnt += 1
        q.append([2*num, cnt])
        q.append([num+1, cnt])
        q.append([num-1, cnt])
        q.append([num-10, cnt])

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans = bfs(N)
    print(f'#{tc} {ans}')