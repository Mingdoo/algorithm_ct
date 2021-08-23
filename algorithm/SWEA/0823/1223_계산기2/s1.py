import sys
sys.stdin = open('input.txt')

operand = ['+', '*']
order = [1, 2]

T = 10
for tc in range(1, 1 + T):
    length = int(input())

    text = input()

    stack = []
    operand_after = ''
    for i in range(length):
        if text[i].isdecimal():
            operand_after += str(text[i])

        else:
            if len(stack) == 0:
                stack.append(text[i])
            else:
                if order[operand.index(stack[-1])] >= order[operand.index(text[i])]:
                    operand_after += stack.pop()
                    stack.append(text[i])
                else:
                    stack.append(text[i])
    while stack:
        operand_after += stack.pop()
    stack_2 = []
    for char in operand_after:
        if char.isdecimal():
            stack_2.append(char)
        else:
            a = int(stack_2.pop())
            b = int(stack_2.pop())
            if char == '+':
                stack_2.append(a + b)
            else:
                stack_2.append(a * b)
    print('#{} {}'.format(tc, stack_2[-1]))