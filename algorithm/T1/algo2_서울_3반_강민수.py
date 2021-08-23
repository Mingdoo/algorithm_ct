T = int(input())

for tc in range(1, T + 1):

    #init block
    N = int(input())
    y_1, x_1, y_2, x_2 = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    #list comprehension으로 matrix의 원하는 row들을 뽑은 다음 원하는 column을 slicing하는 과정.
    sliced_list = [row[x_1 : x_2 + 1] for row in matrix[y_1 : y_2 + 1]]

    #average를 구하는 과정
    total = 0
    length = len(sliced_list) * len(sliced_list[0])
    for arr in sliced_list:
        #제약사항에 sum을 쓰지 말라고는 안하셔서..
        total += sum(arr)

    #소수점 단위 절사
    avg = int(total / length)

    #list comprehension으로 절댓값을 담은 list를 만들기.
    diff_list = [[abs(num - avg) for num in row] for row in sliced_list]

    #(diff_list에 있는 모든 row의 합) 의 합을 summary라고 선언.
    summary = sum([sum(row) for row in diff_list])

    #출력 블록
    print('#{} {} {}'.format(tc, avg, summary))

