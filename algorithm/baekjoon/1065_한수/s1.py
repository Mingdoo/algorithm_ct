def hansu(N):
    cnt = 0
    for i in range(1, N+1):
        arr = list(str(i))
        if len(arr) <= 2:
            cnt += 1
        else:
            cd = int(arr[1]) - int(arr[0])
            for j in range(2, len(arr)):
                if int(arr[j]) - int(arr[j-1]) != cd:
                    break
                if j == len(arr) - 1:
                    cnt += 1
    return cnt

print(hansu(int(input())))
