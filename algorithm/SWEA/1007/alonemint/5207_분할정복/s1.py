T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    N = sorted(list(map(int, input().split())))
    M = list(map(int, input().split()))

    cnt = 0
    for number in M:
        left = 0
        right = n-1

        flag = 'asd'
        while left <= right:
            mid = (left + right) // 2
            if number >= N[mid]:
                if number == N[mid]:
                    cnt += 1
                    break
                else:
                    left = mid + 1
                    if flag == True:
                        break
                    flag = True
            else:
                right = mid - 1
                if flag == False:
                    break
                flag = False
    print(f'#{tc} {cnt}')