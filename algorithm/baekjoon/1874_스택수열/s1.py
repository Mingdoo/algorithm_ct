N = int(input())
seq = ''

put = 1
stack = []
command = []
flag = True
for i in range(N):
    num = int(input())
    while num >= put:
        stack.append(put)
        put += 1
        command.append('+')
    if num == stack[-1]:
        stack.pop()
        command.append('-')
    else:
        flag = False
        break

if flag == False:
    print('NO')
else:
    for i in command:
        print(i)
