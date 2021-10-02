
words = input()
cnt = 0
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alphabet in alphabets:
    if alphabet in words:
        cnt += words.count(alphabet)
        words = words.replace(alphabet, '.')

for word in words:
    if word != '.':
        cnt += 1
print(cnt)
