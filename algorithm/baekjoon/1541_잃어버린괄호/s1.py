import sys
sys.stdin = open('input.txt')

expression = list(input())

status = ''
for i in range(len(expression)):
    if expression[i] == '-':
        status = '-'
    if expression[i] == '+' and status == '-':
        expression[i] = '-'

stack = []
tmp = ''
while expression:
    v = expression.pop(0)
    if v in '-+':
        stack.append(int(tmp))
        stack.append(v)
        tmp = ''
    else:
        tmp += v
stack.append(int(tmp))

tmp = stack.pop(0)
while stack:
    v = stack.pop(0)
    if v in '-+':
        p = stack.pop(0)
        if v == '-':
            tmp = tmp - p
        else:
            tmp = tmp + p
print(tmp)
