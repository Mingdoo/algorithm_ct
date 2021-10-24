from big_O import test
import sys
from random import randint

def quicksort(arr):
    '''
    Best : O(n) Time 모두 같은애일 때
    Average : O(nlog(n)) Time
    Worst : O(nlog(n)) Time
    '''
    if len(arr) <= 1:
        return arr
    pivot = arr[randint(0, len(arr) - 1)]
    l = []
    eq = []
    r = []
    for e in arr:
        if e < pivot:
            l.append(e)
        elif e == pivot:
            eq.append(e)
        else:
            r.append(e)

    return quicksort(l) + eq + quicksort(r)

sys.setrecursionlimit(2500)
print(test(quicksort))