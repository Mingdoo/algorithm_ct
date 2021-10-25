# 몇 번 받을지?
N = int(input())

for _ in range(N):
    vps = list(input())
    #stack
    stack = []
    for i in range(len(vps)):
        if vps[i] == ')' and stack and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(vps[i])
    if stack:
        print('NO')
    else:
        print('YES')