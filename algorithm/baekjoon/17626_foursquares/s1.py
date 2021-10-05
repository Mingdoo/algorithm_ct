import math
N = int(input())

def f(N):
    if int(N**0.5) == N**0.5:
        return 1
    for i in range(1, int(N**0.5) + 1):
        if math.isclose(int((N - i**2)**0.5), (N - i**2)**0.5):
            return 2
    for i in range(1, int(N**0.5) + 1):
        for j in range(1, int((N - i**2)**0.5) + 1):
            if math.isclose(int((N-i**2-j**2)**0.5), (N-i**2-j**2)**0.5):
                return 3
    return 4

print(f(N))
