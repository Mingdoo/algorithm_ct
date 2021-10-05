N = int(input())
sixs = 666
cnt = 0
while True:
    if '666' in str(sixs):
        cnt += 1
    if cnt == N:
        print(sixs)
        break
    sixs += 1

