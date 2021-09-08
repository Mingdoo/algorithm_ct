

def move(dir, x, y, board, checked):
    tmp_x = x
    tmp_y = y
    if dir=='U':
        if y > 0:
            y -= 1
            checked.append(((tmp_y, tmp_x), (y, x)))
            checked.append(((y, x), (tmp_y, tmp_x)))

    elif dir=='D':
        if y < len(board) - 1:
            y += 1
            checked.append(((tmp_y, tmp_x), (y, x)))
            checked.append(((y, x), (tmp_y, tmp_x)))

    elif dir=='R':
        if x < len(board) - 1:
            x += 1
            checked.append(((tmp_y, tmp_x), (y, x)))
            checked.append(((y, x), (tmp_y, tmp_x)))

    else:
        if x > 0:
            x -= 1
            checked.append(((tmp_y, tmp_x), (y, x)))
            checked.append(((y, x), (tmp_y, tmp_x)))



    return (y, x)

def solution(dirs):
    checked = []
    board = [[0] * 11 for _ in range(11)]
    y, x = 5, 5
    for dir in dirs:
        print(y,x)
        y, x = move(dir, x, y, board, checked)


    checked = list(set(checked))

    return len(checked)//2

print(solution('ULURRDLLU'))

