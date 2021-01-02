with open("C:/Projects/other/advent-of-code/day-2/input.txt") as inp:
    data = inp.read().splitlines()

def password_philosophy(x):
    validCounter = 0
    for string in x:
        y = string.split(":")
        password = y[1]

        rule = y[0]
        rule_split = rule.split("-")
        rule_split_2 = rule_split[1].split()

        lowerBound = int(rule_split[0])
        upperBound = int(rule_split_2[0])
        alphaValue = rule_split_2[1]

        if ((password[lowerBound] == alphaValue) or (password[upperBound] == alphaValue)) and not (password[lowerBound] == alphaValue and password[upperBound] == alphaValue):
            validCounter += 1

    return validCounter

print(password_philosophy(data))