import sys
sys.stdin = open('input.txt')

T = int(input())

def tree(n, N):
    global node
    if n <= N:
        tree(2*n, N)
        res[n] = node
        node += 1
        tree(2*n+1, N)

for tc in range(1, T+1):
    N = int(input())
    res = [-1] + [0] * N
    node = 1
    tree(node, N)
    print(f'#{tc} {res[1]} {res[N//2]}')