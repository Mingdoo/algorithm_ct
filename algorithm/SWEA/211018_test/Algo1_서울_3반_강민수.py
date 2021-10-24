for tc in range(1, int(input())+1):
    #결과 값을 받는 res 리스트 생성
    res = [0] * 10
    #글자수는 파이썬은 중요하지 않음
    input()
    #16진수를 받아서 2진수로 변환(결과는 string)
    binary = bin(int(input(), 16))
    cnt = 0

    #개수를 세어주는 알고리즘
    #1. 1이면 개수를 올린다.
    #2. 0이면
        #2.1 지금까지 개수가 양수라면 그 개수번째의 list의 값을 1만큼 올린다.
        #2.2 지금까지 개수가 0이라면 넘어간다.
    #3. 다 세고 나서의 마지막 1의 개수가 남아있다면 그 개수번째의 list의 값을 1만큼 올린다.
    for i in range(len(binary)):
        if binary[i] == '1':
            cnt += 1
        else:
            if cnt > 0:
                res[cnt] += 1
                cnt = 0
    if cnt:
        res[cnt] += 1
    res = res[1:]
    print('#{}'.format(tc), end=' ')
    print(*res)
