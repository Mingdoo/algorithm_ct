def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for i in range(len(times)):
            cnt += mid // times[i]

        if cnt >= n:
            right = mid - 1
        elif cnt < n:
            left = mid + 1

    return left

n = 6
times = [7, 10]
print(solution(n, times))
print('expected : 28')