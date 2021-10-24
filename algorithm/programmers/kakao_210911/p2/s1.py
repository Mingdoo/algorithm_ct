def make_k_number(n, k):
    stack = []
    while n > 0:
        stack.append(str(n % k))
        n = n // k

    res = ''
    while stack:
        res += stack.pop()
    print(res)
    return res

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True
def solution(n, k):

    answer = 0
    my_ans = make_k_number(n, k).split('0')

    for number in my_ans:
        if number != '' and is_prime(int(number)):
            answer += 1
    return answer

print(solution(4480785, 7))

