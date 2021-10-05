import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))

    answer = 0
    while trucks:
        v = trucks.pop()
        compare = v
        idx = 0
        flag = False
        for i in range(len(containers)):
            if 0 <= v - containers[i] < compare:
                idx = i
                compare = v - containers[i]
                flag = True
        if flag:
            answer += containers[idx]
            containers[idx] = 0

    print(f'#{tc} {answer}')