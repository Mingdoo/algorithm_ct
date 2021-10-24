from big_O import test

def insertion_sort(arr):
    '''
    Best : O(n) Time
    Average : O(n^2) Time
    Worst : O(n^2) Time
    '''
    length = len(arr)
    for i in range(1, length):
        tmp = arr[i]
        prev = i - 1
        while prev >= 0 and arr[prev] > tmp:
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = tmp
    return arr

print(test(insertion_sort))