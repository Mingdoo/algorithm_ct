K, N = map(int, input().split())
lines = []
for _ in range(K):
    lines.append(int(input()))

left = 1
right = max(lines)

while left <= right:
    mid = (left + right) // 2
    nums = sum([l // mid for l in lines])
    if nums >= N:
        left = mid + 1
    elif nums < N:
        right = mid - 1

print(right)