import sys
sys.stdin = open('input.txt')

num = list(input())
for i in range(len(num)):
    binary = format(int(num[i], 16), 'b')
    num[i] = '0' * (4 - len(binary)) + binary

num = ''.join(num)

patterns = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

idx = 0
while idx < len(num):
    if num[idx:idx+6] in patterns:
        print(patterns[num[idx:idx+6]], end=' ')
        idx += 6
    else:
        idx += 1