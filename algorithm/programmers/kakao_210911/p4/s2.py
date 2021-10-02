def combinations_3(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            ## array[i+1: ] -> array[i: ] 변경
            for next in combinations_3(array[i:], r-1):
                yield [array[i]] + next
#출처: https://juhee-maeng.tistory.com/91 [simPLE]

def find(res):
    tmp = []
    for j in range(len(res)):
        for i in range(10, -1, -1):
            if res[j][i] > 0:
                tmp.append(res[j])
    return tmp

def solution(n, info):

    lst = [N for N in range(11)]
    a = list(combinations_3(lst, n))
    res = []
    for i in range(len(a)):
        tmp = [[0] for _ in range(11)]
        for j in range(11):
            tmp[j] = a[i].count(j)
        for idx in range(11):
            if tmp[idx] == [0]:
                tmp[idx] = 0

        res.append(tmp)
    maxi = 0
    result = []

    for k in range(len(res)):
        ryan = 0
        apeach = 0
        for j in range(11):
            if info[j] >= res[k][j] and info[j] != 0:
                apeach += (10 - j)
            elif info[j] < res[k][j]:
                ryan += (10 - j)

        gap = ryan - apeach

        if gap >= maxi:
            if gap > maxi:
                while result:
                    result.pop()
            maxi = gap
            result.append(res[k])
    if maxi == 0:
        return [-1]
    if not result:
        return [-1]
    if n == 2:
        return result[0]
    if n == 3:
        return result[0]
    return result[-1]









# n = 5
# info = [2,1,1,1,0,0,0,0,0,0,0]
# print(solution(n, info))
# print("expect = [0,2,2,0,1,0,0,0,0,0,0]")
#
# n = 1
# info = [1,0,0,0,0,0,0,0,0,0,0]
# print(solution(n, info))
# print("expect = [-1]")
#
# n = 9
# info = [0,0,1,2,0,1,1,1,1,1,1]
# print(solution(n, info))
# print("expect = [1,1,2,0,1,2,2,0,0,0,0]")
#
# n = 10
# info = [0,0,0,0,0,0,0,0,3,4,3]
# print(solution(n, info))
# print("expect = [1,1,1,1,1,1,1,1,0,0,2]")
#
# n = 2
# info = [0,1,0,0,0,0,0,0,0,0,1]
# print(solution(n, info))