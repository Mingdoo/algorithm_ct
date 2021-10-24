from big_O import test

def heapify(arr, n, i):
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[parent] < arr[left]:
        parent = left

    if right < n and arr[parent] < arr[right]:
        parent = right

    if i != parent:
        arr[parent], arr[i] = arr[i], arr[parent]
        heapify(arr, n, parent)

def heap_sort(arr):
    '''
    Best : O(nlog(n)) Time
    Average : O(nlog(n)) Time
    Worst : O(nlog(n)) Time
    '''
    length = len(arr)

    for i in range(length // 2, -1, -1):
        heapify(arr, length, i)

    for i in range(length - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr

print(test(heap_sort))