for tc in range(int(input())):
    stack = []
    data = list(input())
    flag = True
    while data:
        v = data.pop(0)
        if v == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        else:
            stack.append(v)

    if not flag or stack:
        print('NO')
    else:
        print('YES')