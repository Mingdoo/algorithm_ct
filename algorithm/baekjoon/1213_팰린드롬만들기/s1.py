data = input()

def hansoo(data):
    my_dict = {}
    for character in data:
        my_dict[character] = my_dict.get(character, 0) + 1
    my_dict = sorted(my_dict.items(), key=lambda x: x[0])

    cnt = 0
    for key, value in my_dict:
        if value % 2 == 1:
            cnt += 1
            if cnt >= 2:
                return 'I\'m Sorry Hansoo'
    center = ''
    if cnt == 1:
        for i in range(len(my_dict)):
            char = my_dict[i][0]
            number = my_dict[i][1]
            if number % 2 == 1:
                center = char
                my_dict[i] = (char, number - 1)

    front = ''
    for i in range(len(my_dict)):
        number = my_dict[i][1] // 2
        for j in range(number):
            front += my_dict[i][0]

    return front + center + front[::-1]

print(hansoo(data))