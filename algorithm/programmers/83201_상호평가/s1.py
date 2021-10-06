def solution(scores):
    answer = ''
    for j in range(len(scores)):
        tmp = []
        M = 0
        m = 1e2
        for i in range(len(scores)):
            tmp.append(scores[i][j])
            if scores[i][j] < m:
                m = scores[i][j]
            if scores[i][j] > M:
                M = scores[i][j]

        for i in range(len(tmp)):
            if tmp[j] == m or tmp[j] == M:
                if tmp[j] == m:
                    if tmp.count(m) == 1:
                        tmp.pop(j)
                        break
                if tmp[j] == M:
                    if tmp.count(M) == 1:
                        tmp.pop(j)
                        break
        avg = sum(tmp)/len(tmp)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))