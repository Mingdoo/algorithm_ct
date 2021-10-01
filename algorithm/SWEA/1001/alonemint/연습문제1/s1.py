def recursive(idx, arr):
    if idx == len(arr) - 1:
        return
    elif arr[idx] > arr[idx+1]:
        arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
        recursive(idx+1, arr)
    else:
        recursive(idx+1, arr)

def selection_sort(arr):
    copied_arr = arr[:]
    for i in range(len(arr)):
        recursive(0, copied_arr)
    return copied_arr

a = [4, 5, 3, 1, 2, 3, 4, 0, 1, 2, 9, 10, 11]
print(f'expected : [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 9, 10, 11]')
print(f'my solution : {selection_sort(a)}')
