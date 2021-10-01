def subset(arr):
    n = len(arr)
    res = []
    for i in range(1<<n):
        tmp = []
        for j in range(n):
            if i & (1 << j):
                tmp.append(arr[j])
        res.append(tmp)
    return res

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
for j in subset(arr):
    if sum(j) == 0:
        print(j)
