with open("./day-3/input.txt") as inp:
    data = inp.read().splitlines()

def toboggan_trajectory(x):
    tree_counter = 0

    row = 0
    column = 0
    while row < len(x):
        if x[row][column] == "#":
            tree_counter += 1

        row += 1
        column += 3

        if row >= len(x):
            return tree_counter
        elif column >= len(x[row]):
            column = column % len(x[row])

print(toboggan_trajectory(data))


