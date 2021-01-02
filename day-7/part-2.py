with open("./day-7/input.txt") as inp:
    data = inp.read().splitlines()

def handy_haversacks(color):
    rule = ''
    for line in data:
        if line[:line.index(' bags')] == color:
            rule = line

    if 'no' in rule:
        return 1

    total = 0

    rule = rule[rule.index('contain')+8:].split(', ')
    for bag in rule:
        words = bag.split()
        counter = int(words[0])
        color = words[1] + ' ' + words[2]

        total += counter * handy_haversacks(color)

    return total + 1

total = handy_haversacks('shiny gold')
print(total - 1)



    