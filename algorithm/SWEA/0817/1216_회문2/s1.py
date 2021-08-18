import sys
sys.stdin = open('input.txt', 'r')

def word_transpose(arr):
    res = []
    for i in range(len(arr)):
        my_word = ''
        for j in range(len(arr)):
            my_word += words[j][i]
        res.append(my_word)
    return res

def slice_word(arr, N, M):
    res = []
    for word in arr:
        for idx in range(N - M + 1):
            res.append(word[idx: idx + M])
    return res

T = 10

for test_case in range(1, T + 1):

    N = 100
    tc = int(input())

    words = []
    for _ in range(N):
        words.append(input())

    #transpose된 words를 concatenate하여 row별, column별 word를 담은 words를 만든다.
    words += word_transpose(words)

    #만들어진 words들 중 길이가 M인 모든 단어들을 sliced_words에 담는다.

    res = 0
    for M in range(1, 100):
        sliced_words = slice_word(words, N, M)
        for word in sliced_words:
            if word == word[::-1]:
                res = M
                break



    print('#{} {}'.format(test_case, res))