import sys
sys.stdin = open('input.txt', 'r')



stack = []
operator = ['*', '/', '+', '-', '(', ')']
isp = [2, 2, 1, 1, 0, -1]
icp = [2, 2, 1, 1, 3, -1]

poly = input()
for char in poly:
    #숫자일 때
    if char.isdecimal():
        print(char, end = '')
    #연산자일때
    else:
        #스택에 뭔가 있고 icp > isp일 때
        if len(stack) and icp[operator.index(char)] >= isp[operator.index(stack[-1])]:
            stack.append(char)
        #아무것도 없으면
        elif len(stack) == 0:
            stack.append(char)
        elif char == ')':
            # (가 나올 때 까지 pop
            while stack[-1] != '(':
                print(stack.pop(), end = '')
            #여는 괄호 버리기
            stack.pop()
        else:
            a = stack.pop()
            stack.append(char)
            print(a, end ='')
while stack:
    print(stack.pop(), end='')
