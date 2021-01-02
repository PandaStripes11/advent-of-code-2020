with open("./day-6/input.txt") as inp:
    data = []
    group = []
    for line in inp:
        if line.isspace():
            data.append(group)
            group = []
            continue

        group.append(line.rstrip("\n"))
    data.append(group)

def custom_customs(x):
    counter = 0

    for group in x:
        dict = {}
        for entry in group:
            for char in entry:
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
        counter += len(dict)

    return counter

print(custom_customs(data))