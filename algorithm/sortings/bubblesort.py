from big_O import test

def bubble_sort(arr):
    '''
    Best : O(n^2) Time
    Average : O(n^2) Time
    Worst : O(n^2) Time
    {'random': 'O(n^2)',
     'sorted': 'O(n^2)',
     'reversed': 'O(n^2)',
     'partial': 'O(n^2)',
     'Ksorted': 'O(n^2)',
     'almost_equal': 'O(n^2)'}
    '''
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

print(test(bubble_sort))
