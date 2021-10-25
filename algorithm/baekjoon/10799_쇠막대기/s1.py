commands = input()

stack = []
cnt = 0
answer = 0
for i in range(len(commands)):
    if commands[i] == '(':
        cnt += 1
    elif commands[i] == ')':
        if commands[i-1] == '(':
            cnt -= 1
            answer += cnt
        else:
            answer += 1
            cnt -= 1
print(answer)
