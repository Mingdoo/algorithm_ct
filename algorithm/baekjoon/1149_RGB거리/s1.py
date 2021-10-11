N = int(input())

rgbs = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    rgbs[i][0] += min(rgbs[i-1][1], rgbs[i-1][2])
    rgbs[i][1] += min(rgbs[i-1][0], rgbs[i-1][2])
    rgbs[i][2] += min(rgbs[i-1][0], rgbs[i-1][1])

print(min(rgbs[N-1][0], rgbs[N-1][1], rgbs[N-1][2]))