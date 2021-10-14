N = int(input())

cnt = 1
continuous_six = 6
tmp = 1
while tmp < N:
    cnt += 1
    tmp += continuous_six
    continuous_six += 6

print(cnt)