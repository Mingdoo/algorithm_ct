import sys
sys.stdin = open('sample_input.txt')
T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    A = []
    B = []
    a = -1
    b = -1
    for i in range(len(cards)):
        if i%2 == 0:
            A.append(cards[i])
            A.sort()
            for j in range(len(A) - 2):
                if A[j+1] - A[j] == A[j+2] - A[j+1]:
                    a = i
                    break
        else:
            B.append(cards[i])
            B.sort()
            for j in range(len(B) - 2):
                if B[j + 1] - B[j] == B[j + 2] - B[j + 1]:
                    b = i
                    break
    res = 0
    if a != -1:
        res = 1

    elif b != -1:
        res = 2

    print(f'#{tc} {res}')
