with open("./day-4/input.txt") as inp:
    data = []
    dict = {}
    for line in inp:
        if line.isspace():
            data.append(dict)
            dict = {}
        
        terms = line.split()
        for term in terms:
            key_and_value = term.split(":")
            key = key_and_value[0]
            value = key_and_value[1]

            dict[key] = value
    data.append(dict)

def passport_processing(x):
    counter = 0
    indexer = 0

    while indexer < len(x):
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        
        for key in x[indexer]:
            values = x[indexer][key]
            if (key == 'byr') and (int(values) <= 2002 and int(values) >= 1920):
                byr = True
            elif (key == 'iyr') and (int(values) <= 2020 and int(values) >= 2010):
                iyr = True
            elif (key == 'eyr') and (int(values) <= 2030 and int(values) >= 2020):
                eyr = True
            elif (key == 'hgt') and (values[-2:] == "in" or values[-2:] == "cm"):
                if values[-2:] == "in" and (int(values[:-2]) <= 76 and int(values[:-2]) >= 59):
                    hgt = True
                elif values[-2:] == "cm" and (int(values[:-2]) <= 193 and int(values[:-2]) >= 150):
                    hgt = True
            elif (key == 'hcl') and (values[0] == "#"):
                hcl = True
                for char in values:
                    if char.isnumeric():
                        continue
                    elif char == 'a' or char == 'b' or char == 'c' or char == 'd' or char == 'e' or char == 'f':
                        continue
                    hcl == False
            elif (key == 'ecl') and (values == 'amb' or values == 'blu' or values == 'brn' or values == 'gry' or values =='grn' or values == 'hzl' or values == 'oth'):
                ecl = True
            elif (key == 'pid') and (len(values) == 9) and (values.isnumeric()):
                pid = True
        
        if (byr and iyr and eyr and hgt and hcl and ecl and pid) == True:
            counter += 1   

        indexer += 1  
    return counter

print(passport_processing(data))