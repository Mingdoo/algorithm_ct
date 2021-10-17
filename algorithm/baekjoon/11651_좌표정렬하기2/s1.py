N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda a:(a[1],a[0]))
for element in lst:
    print(*element)