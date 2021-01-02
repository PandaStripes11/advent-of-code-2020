with open("./day-5/input.txt") as inp:
    data = inp.read().splitlines()

def binary_boarding(x):
    largest_id = -1
    for string in x:
        column_chars = string[-3:]
        row_chars = string[:-3]

        F = 0
        B = 127
        for char in row_chars:
            if char == 'F':
                B = B - ((B - F) // 2) - 1
                # print("B: " + str(B))
            if char == 'B':
                F = ((B - F) // 2) + F + 1
                # print("F: " + str(F))

        L = 0
        R = 7
        for char in column_chars:
            if char == 'L':
                R = R - ((R - L) // 2) - 1
                # print("R: " + str(R))
            if char == 'R':
                L = ((R - L) // 2) + L + 1
                # print("L: " + str(L))
        if (F * 8 + L) > largest_id:
            largest_id = F * 8 + L

    return largest_id

print(binary_boarding(data))