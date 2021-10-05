N = int(input())
words = [[] for _ in range(51)]
for _ in range(N):
    word = input()
    words[len(word)].append(word)

for i in range(len(words)):
    words[i] = list(set(words[i]))
    words[i].sort()

for i in range(1, 51):
    if words[i]:
        print(*words[i], sep='\n')

