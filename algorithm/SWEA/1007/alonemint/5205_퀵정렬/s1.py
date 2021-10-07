def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]

    left = [element for element in arr[1:] if element <= pivot]
    right = [element for element in arr[1:] if element > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quicksort(arr)
    print(arr)
    print(f'#{tc} {arr[N//2]}')