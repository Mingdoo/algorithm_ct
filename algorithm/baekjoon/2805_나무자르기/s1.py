N, M = map(int, input().split())
trees = list(map(int, input().split()))

left = 1
right = max(trees)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for tree in trees:
        cnt += max(tree - mid, 0)
    if cnt >= M:
        left = mid + 1
    elif cnt < M:
        right = mid - 1

print(right)