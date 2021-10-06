import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda a: a[1])

    time = 0
    cnt = 0
    while time <= 24:
        flag = False
        for i in range(N):
            if arr[i][0] >= time:
                task = arr.pop(i)
                cnt += 1
                time = task[1]
                flag = True
                break
        if not flag:
            time += 1
    print(f'#{tc} {cnt}')
