import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):

    text = input()

    cnt = 0
    res = 0

    for idx in range(len(text)):
        # 열고 닫음에서 +1, -1을 해준다.
        if text[idx] == '(':
            cnt += 1

        else:
            cnt -= 1
            # 레이저로 자르면 ()가 나오니까 쌓인 스택만큼 더해준다.
            if text[idx - 1] == '(':
                res += cnt

            # 막대의 끝 부분이 와서 더해주기.
            else:
                res += 1

    print('#{} {}'.format(test_case, res))
