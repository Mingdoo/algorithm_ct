L = int(input())
words = input()
alpha = '0abcdefghijklmnopqrstuvwxyz'
H = 0
for i in range(L):
    H += alpha.index(words[i]) * 31**i

print(H % 1234567891)