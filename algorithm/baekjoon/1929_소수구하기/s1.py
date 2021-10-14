e = [True for i in range(1000000)]
def era():
    e[1] = False
    for i in range(2, 1001):
        if e[i] == True:
            for j in range(i * 2, 1000000, i):
                e[j] = False
era()

N, M = map(int, input().split())

for i in range(N, M+1):
    if e[i]:
        print(i)