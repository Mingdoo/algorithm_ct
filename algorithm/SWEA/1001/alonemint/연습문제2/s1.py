arr = [1,2,4,7,8,3]
p = [0] * len(arr)
used = [0] * len(arr)
result = []
flag = True

def perm(n, k):
    global flag
    if n == k:
        if p[0] == p[1] == p[2] and p[4] - p[3] == 1 and p[5] - p[4] == 1:
            print(f'baby-gin : {p}')
            flag = False
    elif flag:
        for i in range(n):
            if not used[i]:
                p[k] = arr[i]
                used[i] = True
                perm(n, k+1)
                used[i] = False

perm(6, 0)
if flag:
    print('not baby-gin')