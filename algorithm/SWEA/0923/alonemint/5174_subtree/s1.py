import sys
sys.stdin = open('input.txt')

T = int(input())


def count(idx, array):
    global cnt
    if array[idx] != -1:
        cnt += 1
        if 2*idx + 1 <= len(array):
            count(2*idx, array)
            count(2*idx+1, array)
    else:
        return

for tc in range(1, T+1):
    E, N = map(int, input().split())

    user_input = list(map(int, input().split()))
    result = [-1] * (2**100)
    for i in range(E):
        parent = user_input[2*i]
        if parent not in result:
            result[i+1] = parent

        child = user_input[2*i+1]
        if result[2 * result.index(parent)] == -1:
            result[2 * result.index(parent)] = child
        else:
            result[2 * result.index(parent) + 1] = child
    idx = result.index(N)
    cnt = 0
    count(idx, result)
    print(f'#{tc} {cnt}')

