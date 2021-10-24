from big_O import test

def selection_sort(arr):
    '''
    Best : O(n^2) Time
    Average : O(n^2) Time
    Worst : O(n^2) Time
    '''
    length = len(arr)
    for i in range(length):
        index = i
        for j in range(i+1, length):
            if arr[j] < arr[index]:
                index = j
        arr[index], arr[i] = arr[i], arr[index]
    return arr

print(test(selection_sort))
