N = int(input())
names = [[] for _ in range(201)]
for i in range(N):
    age, name = input().split()
    age = int(age)
    names[age].append([age, name])

for arr in names:
    if arr:
        for age, name in arr:
            print(age, name)