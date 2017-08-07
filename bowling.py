def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == '/':
                result += 10 - get_value(game[i - 1]) + (get_value(game[i + 1]))
            else:
                if game[i + 2] == '/':
                    result += 20
                else:
                    result += 10 + get_value(game[i + 1]) + get_value(game[i + 2])
                    in_first_half = True
                    frame += 1
        else:
            result += get_value(game[i])
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char in ("xX/"):
        return 10
    elif char == '-':
        return 0
    char = int(char)
    if char >= 0 or char < 10:
        return char
    else:
        raise ValueError()
