def solution(price, money, count):
    ans = 0
    for i in range(1, count+1):
        ans += i*price
    return ans - money

solution(3, 20, 4)