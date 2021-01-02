with open("./day-3/input.txt") as inp:
    data = inp.read().splitlines()
    
def toboggan_trajectory(x, incrementRow, incrementColumn):
    tree_counter = 0

    row = 0
    column = 0
    while row < len(x):
        if x[row][column] == "#":
            tree_counter += 1

        row += incrementRow
        column += incrementColumn

        if row >= len(x):
            return tree_counter
        elif column >= len(x[row]):
            column = column % len(x[row])

a = toboggan_trajectory(data, 1, 1)
b = toboggan_trajectory(data, 1, 3)
c = toboggan_trajectory(data, 1, 5)
d = toboggan_trajectory(data, 1, 7)
e = toboggan_trajectory(data, 2, 1)

print(a * b * c * d * e)
