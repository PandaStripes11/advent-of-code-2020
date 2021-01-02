with open("./day-7/input.txt") as inp:
    data = inp.read().splitlines()

all_bags = []
unique_bags = []
def handy_haversacks(color):
    global all_bags
    global unique_bags
    bag_lines = [line for line in data if color in line and line.index(color) != 0]

    if len(bag_lines) == 0:
        return []
    else:
        colors = [line[:line.index(' bags')] for line in bag_lines]
        colors = [color for color in colors if color not in all_bags]

        for color in colors:
            all_bags.append(color)
            more_bags = handy_haversacks(color)

            all_bags += more_bags

        for color in all_bags:
            if color not in unique_bags:
                unique_bags.append(color)

        return unique_bags
    
colors = handy_haversacks('shiny gold')
print(len(colors))
