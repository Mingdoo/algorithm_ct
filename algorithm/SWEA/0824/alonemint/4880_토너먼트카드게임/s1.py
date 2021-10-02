import sys
sys.stdin = open('input.txt')

T = int(input())

def fight(first, second):
    if first[1] == 1:
        if second[1] == 3:
            return first
    if first[1] == 2:
        if second[1] == 1:
            return first
    if first[1] == 3:
        if second[1] == 2:
            return first
    if first[1] == second[1]:
        return first

    else:
        return second

#divide & conquer
def tournament(arr):

    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return fight(arr[0], arr[1])

    mid = (len(arr) - 1) // 2 + 1
    left_winner = tournament(arr[:mid])
    right_winner = tournament(arr[mid:])
    return fight(left_winner, right_winner)

for tc in range(1, T + 1):

    N = int(input())
    #카드를 받은 사람 순서대로 1, 2, 3, 4, ...
    cards = list(enumerate(map(int, input().split()), start = 1))
    print('#{} {}'.format(tc, tournament(cards)[0]))