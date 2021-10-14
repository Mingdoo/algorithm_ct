while True:
    words = input()
    if words == '.':
        break
    else:
        stack = []
        flag = True
        for word in words:
            if word == '(' or word == '[':
                stack.append(word)
            elif word == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    flag = False
                    break
            elif word == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    flag = False
                    break
        if stack:
            print('no')
        if flag and not stack:
            print('yes')