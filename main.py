def grid(v):
    print("---------")
    print('|', v[0], v[1], v[2], '|')
    print('|', v[3], v[4], v[5], '|')
    print('|', v[6], v[7], v[8], '|')
    print("---------")

def get_user_input(v):
    print("Enter the coordinates (row and column, separated by a space): ")
    while True:
        user_input = input()

        try:
            row_input, col_input = user_input.split()
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
            continue

        if not user_input.replace(" ", "").isdigit():
            print("You should enter numbers!")
            continue

        row_input, col_input = user_input.split()

        if not row_input.isdigit() or not col_input.isdigit():
            print("You should enter numbers!")
            continue

        row, col = int(row_input), int(col_input)

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        i = col + 2
        j = row - 1
        index = (j * 3 + i) - 3

        if not v[index] == "_":
            print("This cell is occupied! Choose another one!")
            continue

        return index

def win(v):
    x_sum = o_sum = 0
    x_wins = o_wins = 0
    # vertical
    for i in range(0, 9, 3):
        if (v[i] != "_") and (v[i] == v[i + 1]) and (v[i + 1] == v[i + 2]):
            if v[i] == "X":
                x_wins += 1
            elif v[i] == "O":
                o_wins += 1
    # horizontal
    for i in range(0, 3):
        if (v[i] != "_") and (v[i] == v[i + 3]) and (v[i + 3] == v[i + 6]):
            if v[i] == "X":
                x_wins += 1
            elif v[i] == "O":
                o_wins += 1
    # diagonally
    if (v[0] == v[4] == v[8]) or (v[2] == v[4] == v[6]):
        if v[4] == "X":
            x_wins += 1
        elif v[4] == "O":
            o_wins += 1

    # count xo
    for i in v:
        if i == 'X':
            x_sum += 1
        elif i == 'O':
            o_sum += 1

    # check
    if abs(x_sum - o_sum) > 1 or (x_wins > 0 and o_wins > 0):
        return "Impossible"
    elif "_" not in v and o_wins < 1 and x_wins < 1:
        return "Draw"
    elif x_wins == 1:
        return "X wins"
    elif o_wins == 1:
        return "O wins"
    elif "_" in v:
        return "Game not finished"

def switch_player(current_player):
    return "O" if current_player == "X" else "X"

v = ["_" for _ in range(9)]
current_player = "X"

while True:
    grid(v)
    index = get_user_input(v)
    v[index] = current_player

    result = win(v)
    if result !="Game not finished":
        grid(v)
        print(result)
        break
    current_player = switch_player(current_player)
#change
