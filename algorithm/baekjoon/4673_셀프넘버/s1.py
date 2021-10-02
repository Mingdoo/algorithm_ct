arr = [0 for _ in range(10001)]

for i in range(1, 10001):
    if arr[i] == 0:
        print(i)
    tmp = i
    while tmp <= 10000:
        arr[tmp] = -1
        for char in str(tmp):
            tmp += int(char)
