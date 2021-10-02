def solution(s):
    answer = -1

    stack = [s[0]]
    for char in s[1:]:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return 0
    else:
        return 1