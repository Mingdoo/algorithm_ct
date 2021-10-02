def solution(n):
    stack = []

    while n > 0:

        if n % 3 == 0:
            stack.append(4)
            n = n // 3 - 1

        elif n % 3 == 1:
            stack.append(1)
            n = n // 3

        elif n % 3 == 2:
            stack.append(2)
            n = n // 3

    answer = ''
    while stack:
        answer += str(stack.pop())

    return answer

print(solution(10))