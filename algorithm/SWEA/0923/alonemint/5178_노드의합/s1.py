import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+2)
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    for i in range(len(tree)-1, 0, -1):
        if tree[i] == 0 and 2*i+1 < len(tree):
            tree[i] = tree[2*i] + tree[2*i+1]
    print(f'#{tc} {tree[L]}')


