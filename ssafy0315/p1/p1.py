# import sys
# sys.stdin = open('input.txt')

visited = [0] * 10
N = 10
answer = 1e9
gates = [3, 5, 9]
people = [5, 2, 2]

def dfs(idx, number, cnt, tmp):
    global answer

    print(cnt)
    if cnt - 1 >= number:
        print(tmp)
        print(visited)
        answer = tmp
        return

    if visited[idx] == 0 and N - idx + cnt - 1 >= number:
        if cnt <= people[0]:
            bias = abs(gates[0] - idx) + 1
        elif people[0] < cnt <= people[0] + people[1]:
            bias = abs(gates[1] - idx) + 1
        else:
            bias = abs(gates[2] - idx) + 1

        visited[idx] = 1
        dfs(idx + 1, number, cnt + 1, tmp + bias)
        visited[idx] = 0
        dfs(idx + 1, number, cnt, tmp)

dfs(0, sum(people), 1, 0)





# T = int(input())
#
# for tc in range(1, T+1):
#     gates = []
#     people = []
#     N = int(input())
#     field = [-1] * N
#
#     for _ in range(3):
#         a, b = map(int, input().split())
#         gates.append(a - 1)
#         people.append(b - 1)
#
#     answer = 1e9
#
#     visited = [0]*N
#     # dfs(0, sum(people), 0, 0)
#
#
