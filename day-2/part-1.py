with open("C:/Projects/other/advent-of-code/day-2/input.txt") as inp:
    data = inp.read().splitlines()

def password_philosophy(x):
    validCounter = 0
    for string in x:
        counter = 0

        y = string.split(":")
        password = y[1]

        rule = y[0]
        rule_split = rule.split("-")
        rule_split_2 = rule_split[1].split()

        lowerBound = rule_split[0]
        upperBound = rule_split_2[0]
        alphaValue = rule_split_2[1]
        
        for char in password:
            if char == alphaValue:
                counter += 1

        if counter <= int(upperBound) and counter >= int(lowerBound):
            validCounter += 1

    return validCounter

print(password_philosophy(data))
        

            
