def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    for i in range(len(report)):
        report[i] = report[i].split()

    counter = {}
    mail = {}
    for id in id_list:
        counter[id] = counter.get(id, 0)
        mail[id] = mail.get(id, 0)

    for i in range(len(report)):
        counter[report[i][1]] = counter.get(report[i][1], 0) + 1

    for person, count in counter.items():
        if count >= k:
            for lst in report:
                if person == lst[1]:
                    mail[lst[0]] = mail.get(lst[0], 0) + 1
    return list(mail.values())

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(list(solution(id_list, report, k).values()))