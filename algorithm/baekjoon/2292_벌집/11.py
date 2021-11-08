def solution(nums):
    M, m = max(nums), min(nums)
    length = len(nums)
    min_index = set()
    max_index = set()
    for i in range(length):
        if nums[i] == M:
            max_index.add(i)
        if nums[i] == m:
            min_index.add(i)
    answer = 1e9
    for i in min_index:
        for j in max_index:
            if abs(i-j) + 1 < answer:
                answer = abs(i-j) + 1
    return answer

print(solution([4,6,8,1,0,9,3,4,7,3]))