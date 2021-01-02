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
            
            if key == 'byr':
                byr = True
            elif key == 'iyr':
                iyr = True
            elif key == 'eyr':
                eyr = True
            elif key == 'hgt':
                hgt = True
            elif key == 'hcl':
                hcl = True
            elif key == 'ecl':
                ecl = True
            elif key == 'pid':
                pid = True
        
        if (byr and iyr and eyr and hgt and hcl and ecl and pid) == True:
            counter += 1   

        indexer += 1  
    return counter 

print(passport_processing(data))





