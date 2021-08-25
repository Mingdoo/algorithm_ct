import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    #operand_after에 후위연산자를 저장
    operand_after = input().split()
    boolean = True
    stack_2 = []

    for char in operand_after:
        if char == '.':
            break

        elif char.isdecimal():
            stack_2.append(char)

        else:
            try:
                b = int(stack_2.pop())
                a = int(stack_2.pop())
            except IndexError:
                stack_2.append('error')
                break

            if char == '+':
                stack_2.append(a + b)
            elif char == '*':
                stack_2.append(a * b)
            elif char == '/':
                stack_2.append(int(a / b))
            elif char == '-':
                stack_2.append(a - b)

    if len(stack_2) > 1:
        stack_2.append('error')
    print('#{} {}'.format(tc, stack_2[-1]))