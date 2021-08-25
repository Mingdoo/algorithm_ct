import sys
sys.stdin = open('input.txt')

operator = ['*', '/', '+', '-', '(', ')']
isp = [2, 2, 1, 1, 0, -1]
icp = [2, 2, 1, 1, 3, -1]

T = 10
for tc in range(1, 1 + T):
    length = int(input())

    stack = []
    poly = input()
    operand_after = ''
    for char in poly:
        # 숫자일 때
        if char.isdecimal():
            operand_after += char
        # 연산자일때
        else:
            # 스택에 뭔가 있고 icp > isp일 때
            if len(stack) and icp[operator.index(char)] > isp[operator.index(stack[-1])]:
                stack.append(char)
            # 아무것도 없으면
            elif len(stack) == 0:
                stack.append(char)
            elif char == ')':
                # (가 나올 때 까지 pop
                while stack[-1] != '(':
                    operand_after += stack.pop()
                # 여는 괄호 버리기
                stack.pop()
            else:
                operand_after += stack.pop()
                stack.append(char)

    while stack:
        operand_after += stack.pop()

    print(operand_after)
    stack_2 = []
    for char in operand_after:
        if char.isdecimal():
            stack_2.append(char)
        else:
            b = int(stack_2.pop())
            a = int(stack_2.pop())
            if char == '+':
                stack_2.append(a + b)
            else:
                stack_2.append(a * b)
    print('#{} {}'.format(tc, stack_2[-1]))