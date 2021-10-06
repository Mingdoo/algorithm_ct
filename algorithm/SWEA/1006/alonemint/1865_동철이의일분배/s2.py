import sys
sys.stdin = open('input.txt')

def searching(N, prob, cand):
    global answer
    left = len(cand)

    if prob <= answer:
        return
    else:
        if len(cand) == 0:
            if prob > answer:
                answer = prob
            return
        else:
            for i in cand:
                cand.remove(i)
                searching(N, prob * lst[N - left][i], cand)
                cand.add(i)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(lambda a: int(a)/100, input().split())) for _ in range(N)]
    answer = 0
    searching(N, 1, set(range(N)))
    print('#{} {:f}'.format(tc, answer*100))