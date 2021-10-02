word = 'V__V'
mo = 'AEIOU'
ja = 'CBDFGHJKLMNPQRSTVWXYZ'
alphabet = mo + ja
word = list(word)

def find_underbar(word):
    for i in range(len(word)):
        if word[i] == '_':
            return i
    return None

def check(word):
    m = 0
    j = 0
    l = 0
    for i in range(len(word)):
        if word[i] in mo:
            if j > 0:
                j = 0
            m += 1
            if m >= 3:
                return 0
        elif word[i] in ja:
            if word[i] == 'L':
                l += 1
            if m > 0:
                m = 0
            j += 1
            if j >= 3:
                return 0
        elif word[i] == '_':
            m = 0
            j = 0
            return 1
    return 1 if l > 0 else 0

cnt = 0
under_bar = set()
res = []
my_bool = False
def funny_word(word):
    global cnt
    idx = find_underbar(word)

    if idx == None:
        cnt += check(word)

    else:
        under_bar.add(idx)
        for alpha in alphabet:
            word[idx] = alpha
            if check(word):
                funny_word(word)
            word[idx] = '_'

funny_word(word)
print(cnt)