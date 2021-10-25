def dfs(v, steps):
    global answer
    first_set = set()
    second_set = set()
    for i in range(len(steps)):
        first_set.add(steps[i][0])
        second_set.add(steps[i][1])
    if first_set == second_set and len(first_set) > len(answer):
        answer = first_set

    for j in range(v+1, N):
        dfs(j, steps + [numbers[j]])
N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

numbers = list(enumerate(numbers, start=1))
answer = []

for i in range(N):
    dfs(i, [numbers[i]])

print(len(answer))
for e in sorted(answer):
    print(e)