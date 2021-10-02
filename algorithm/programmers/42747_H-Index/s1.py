def solution(citations):
    answer = 0
    citations = sorted(citations)
    for i in range(1, max(citations) + 1):
        cnt = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                cnt += 1
        if i <= cnt:
            answer = i
    return answer

print('expected : 3 \nmy_sol :', end=' ')
print(solution([3,0,6,1,5]))