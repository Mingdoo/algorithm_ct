def merge(A, B):
    global ans
    if A[-1] > B[-1]:
        ans += 1
    len_a, len_b = len(A), len(B)
    res = [0] * (len_a + len_b)
    a_idx = b_idx = put = 0
    while a_idx < len_a and b_idx < len_b:
        if A[a_idx] <= B[b_idx]:
            res[put] = A[a_idx]
            put += 1
            a_idx += 1
        else:
            res[put] = B[b_idx]
            put += 1
            b_idx += 1
    while a_idx < len_a:
        res[put] = A[a_idx]
        put += 1
        a_idx += 1
    while b_idx < len_b:
        res[put] = B[b_idx]
        put += 1
        b_idx += 1
    return res

def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    return merge(left, right)
T = int(input())
for tc in range(1, T+1):
    ans = 0
    input()
    lst = list(map(int, input().split()))
    lst = mergesort(lst)
    print(f'#{tc} {lst[len(lst)//2]} {ans}')