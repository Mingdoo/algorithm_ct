def get_max(arr):
    '''
    returns maximum value of given array/list

    :param arr:
    :return: max value of given array/list
    '''
    if len(arr) == 0:
        return None
    maximum = arr[0]
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

def get_min(arr):
    '''
    returns minimum value of given array/list

    :param arr:
    :return: min value of given array/list
    '''
    if len(arr) == 0:
        return None
    minimum = arr[0]
    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum

T = int(input())

for tc in range(1, T + 1):

    #init block
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    #algorithm block
    print('#{}'.format(tc), end = ' ')
    res = []

    # N-M+1 번 만큼 반복. (index error를 야기할 수 있기 때문.)
    for i in range(N - M + 1):
        #list를 잘라서
        sliced_list = arr[i : i + M]

        #차이를 구한 다음
        diff = get_max(sliced_list) - get_min(sliced_list)

        #res에 append
        res.append(diff)

    #print(diff, end = ' ')로 하면 마지막 숫자 뒤에도 띄어쓰기가 나와서 아래와 같은 방법으로 했음.
    print(*res, sep = ' ')