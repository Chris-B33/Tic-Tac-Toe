def print_grid(a):
    print("---------")
    print("|", a[0][0], a[0][1], a[0][2], "|")
    print("|", a[1][0], a[1][1], a[1][2], "|")
    print("|", a[2][0], a[2][1], a[2][2], "|")
    print("---------")


def menu(t):
    while True:
        move = list(map(int, input("Enter the coordinates: ").replace(' ', '')))
        x = move[0] - 1
        y = move[1] - 1
        # Check if valid input
        if type(x) != int or type(y) != int:
            print("You should enter numbers!")
            continue

        elif not 0 <= x <= 2 or not 0 <= y <= 2:
            print("Coordinates should be from 1 to 3!")
            continue

        elif grid[x][y] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        else:
            enter(grid, (x, y), t)
            break


def enter(g, p, player):
    x = p[0]
    y = p[1]
    g[x][y] = player


def three_in_a_row(g):  # Check if either side has won
    x_wins = False
    o_wins = False

    # Check horizontals
    for i in range(3):
        if g[i][0] == g[i][1] == g[i][2] == "X" and "_" not in g[i]:
            x_wins = True
        elif g[i][0] == g[i][1] == g[i][2] == "O" and "_" not in g[i]:
            o_wins = True

    # Check verticals
    for i in range(3):
        if g[0][i] == g[1][i] == g[2][i] == "X" and "_" not in g[i]:
            x_wins = True
        elif g[0][i] == g[1][i] == g[2][i] == "O" and "_" not in g[i]:
            o_wins = True

    # Check diagonals
    if g[0][0] == g[1][1] == g[2][2] == "X":
        x_wins = True
    elif g[0][0] == g[1][1] == g[2][2] == "O":
        o_wins = True
    if g[2][0] == g[1][1] == g[0][2] == "X":
        x_wins = True
    elif g[2][0] == g[1][1] == g[0][2] == "O":
        o_wins = True

    # Determine outcome
    if x_wins and o_wins or g.count("X") >= (g.count("O") + 2) or g.count("O") >= (g.count("X") + 2):
        return "Impossible"

    elif x_wins:
        return "X"

    elif o_wins:
        return "O"

    else:
        return False


grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
print_grid(grid)
turn = "X"
while True:
    menu(turn)
    print_grid(grid)
    turn = "X" if turn == "O" else "O"

    # Check condition of grid
    if three_in_a_row(grid) == "Impossible":
        print("Impossible")
        break

    elif three_in_a_row(grid) == "X":
        print("X wins")
        break

    elif three_in_a_row(grid) == "O":
        print("O wins")
        break

    elif not three_in_a_row(grid) and "_" not in grid[0] and "_" not in grid[1] and "_" not in grid[2]:
        print("Draw")
        break
