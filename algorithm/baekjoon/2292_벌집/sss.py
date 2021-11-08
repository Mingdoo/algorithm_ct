from collections import defaultdict

def solution(address_book):
    answer = 0
    phone_book = defaultdict(set)
    for name, number in address_book:
        number = number.replace('-', '')
        number = number.replace(' ', '')
        phone_book[name].add(number)
    for item in phone_book.values():
        if len(item) > 1:
            answer += len(item)
    return answer

add_book = [['kim', '012-423-0044'], ['park', '042-512-4555'], ['choi', '555-523'], ['kim', '444-524'], ['kim', '0124230044']]
print(solution(add_book))