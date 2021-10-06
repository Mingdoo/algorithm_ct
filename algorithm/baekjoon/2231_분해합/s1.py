N = int(input())

flag = False
for i in range(1, N):
    res = i
    for char in str(i):
        res += int(char)
    if res == N:
        print(i)
        flag = True
        break

if flag == False:
    print(0)