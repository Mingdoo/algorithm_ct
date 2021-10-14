N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])
for element in lst:
    print(*element)