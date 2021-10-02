import math

def solution(fees, records):
    answer = []
    for i in range(len(records)):
        tmp = records[i].split()
        records[i] = [int(tmp[0][:2]) * 60 + int(tmp[0][3:]), tmp[1], tmp[2]]
    time_table = {}
    fee_table = {}
    stack = []
    for i in range(len(records)):
        if records[i][2] == 'IN':
            stack.append(records[i])
        else:
            for j in range(len(stack)):
                if records[i][1] in stack[j]:
                    v = stack.pop(j)
                    time = records[i][0] - v[0]
                    time_table[records[i][1]] = time_table.get(records[i][1], 0) + time

                    break
    while stack:
        v = stack.pop()
        time_table[v[1]] = time_table.get(v[1], 0) + (1439 - v[0])
    print(time_table)

    for id, time in time_table.items():
        if time <= fees[0]:
            fee_table[id] = fee_table.get(id, 0) + fees[1]
        else:
            fee_table[id] = fee_table.get(id, 0) + fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]

    print(fee_table)
    fee_table = dict(sorted(fee_table.items(), key=lambda x: x[0]))
    return list(fee_table.values())


#기본시간, 기본요금, 단위시간, 단위요금
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))
# records = [[334, '5961', 'IN'], [360, '0000', 'IN'], [394, '0000', 'OUT'], [479, '5961', 'OUT'], [479, '0148', 'IN'], [1139, '0000', 'IN'], [1149, '0148', 'OUT'], [1379, '5961', 'IN'], [1380, '5961', 'OUT']]
