import sys
sys.stdin = open('input.txt')

repeat = int(input())

for i in range(repeat):

    length = int(input())
    state = list(map(int, input().split()))
    height = [0] * 100
    for depth in range(length):
        for floor in range(state[depth]):
            if height[floor] == 0:
                height[floor] = length - depth - 1
            else:
                height[floor] -= 1
    max = 0
    for element in height:
        if element > max:
            max = element
    print(max)

