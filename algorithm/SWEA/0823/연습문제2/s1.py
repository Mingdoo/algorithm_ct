arr = [1, 2, 3]
N = len(arr)
checked = [0] * N

def powerset(idx):

    if idx == N:

        for i in range(N):
            if checked[i]:
                print(arr[i], end = ' ')
        print()
        return

    checked[idx] = 1
    powerset(idx + 1)

    checked[idx] = 0
    powerset(idx + 1)

powerset(0)

