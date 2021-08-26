import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())

    Ci = list(enumerate(map(int, input().split()), start = 1))

    queue = []

    for i in range(N):
        queue.append(Ci.pop(0))

    while queue:
        v = queue.pop(0)
        if v[1] // 2 == 0:
            if len(Ci):
                queue.append(Ci.pop(0))
        else:
            queue.append((v[0], v[1] // 2))
    print('#{} {}'.format(tc, v[0]))



