from big_O import test

def counting_sort(arr):
    '''
    Best : O(n) Time
    Average : O(n) Time
    Worst : O(n) Time

    라고 나오지만....!!!!!!!
    실제로는 O(n+k) // k는 최댓값
    '''
    res = []
    mx = max(arr)
    count = [0] * (mx + 1)
    for e in arr:
        count[e] += 1

    for i in range(mx+1):
        if count[i]:
            for _ in range(count[i]):
                res.append(i)
    return res

print(counting_sort([5,4,3,2,1,2,3,4,5]))