import time
Arr = [i for i in range(1, 100)]

N = len(Arr)

checked = [0] * N
result = []
RS = sum(Arr)

def powerset(idx, s, t, RS):

    if s > t:
        return

    elif s == t:
        for i in range(N):
            if checked[i]:
                print(Arr[i], end = ' ')
        print()
        return

    elif s + RS < t:
        return

    if idx == N:
        return

    checked[idx] = 1
    powerset(idx + 1, s + Arr[idx], t, RS - Arr[idx])

    checked[idx] = 0
    powerset(idx + 1, s, t, RS)

a = time.time()
powerset(0, 0, 60, RS)
print(time.time() - a)