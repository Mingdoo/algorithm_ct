from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = deque(list(enumerate(map(int, input().split()))))
    answer = 0
    while q:
        c_idx, c_val = q.popleft()
        flag = True
        for idx, val in q:
            if val > c_val:
                flag = False
                break
        if flag:
            answer += 1
            if M == c_idx:
                print(answer)
                break
        else:
            q.append((c_idx, c_val))

