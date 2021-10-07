def quicksort(arr, left, right):
    if left < right:
        s = partition(arr, left, right)
        quicksort(arr, left, s-1)
        quicksort(arr, s+1, right)

def partition(arr, left, right):
    pivot = arr[left]
    head = left + 1
    tail = right

    while head <= tail:
        while head <= tail and arr[head] <= pivot:
            head += 1
        while head <= tail and arr[tail] >= pivot:
            tail -= 1
        if head <= tail:
            arr[head], arr[tail] = arr[tail], arr[head]

    arr[left], arr[tail] = arr[tail], arr[left]
    return tail

T = int(input())
for tc in range(1, T+1):
    length = int(input())
    lst = list(map(int, input().split()))
    quicksort(lst, 0, len(lst) - 1)
    print(f'#{tc} {lst[length//2]}')