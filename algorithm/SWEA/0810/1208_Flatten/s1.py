import sys
sys.stdin = open('input.txt')

def get_max(arr):
    if len(arr) == 0:
        return None
    else:
        max = arr[0]
        for element in arr:
            if element > max:
                max = element
        return max

def get_min(arr):
    if len(arr) == 0:
        return None
    else:
        min = arr[0]
        for element in arr:
            if element < min:
                min = element
        return min

T = 10
for test_case in range(1, T + 1):

    number = int(input())
    height = list(map(int, input().split()))

    for i in range(number):
        #최고 높이가 여러개인 것은 중요하지 않다.
        #왜냐면 한번씩 하니까!
        max_idx = height.index(get_max(height))
        min_idx = height.index(get_min(height))

        height[max_idx] -= 1
        height[min_idx] += 1

    print('#{} {}'.format(test_case, get_max(height) - get_min(height)))