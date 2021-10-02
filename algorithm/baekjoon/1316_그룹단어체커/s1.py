import sys
N = int(sys.stdin.readline())

cnt = 0
for i in range(N):
    alphabet = ['a','b','c','d','e','f','g',
                'h','i','j','k','l','m','n',
                'o','p','q','r','s','t','u',
                'v','w','x','y','z']
    word = sys.stdin.readline()

    tmp = ''
    flag = False
    for char in word:
        if tmp == '':
            tmp = char
        elif tmp == char:
            continue
        else:
            if tmp in alphabet:
                alphabet.remove(tmp)
                tmp = char
                flag = True
            else:
                flag = False
                break
    if flag:
        cnt += 1
print(cnt)
