#############################
# Advent of Code 2020 Challenge
# Day 4
#############################

#Combined Part 1 and Part 2 solution inputs
def passportChecker(passportList):
    tempList = passportList.read().split('\n\n')
    tempList = [x.replace('\n', ' ').split() for x in tempList]
    passports = []
    for uncheckedPassport in tempList:
        passports.append(dict(data.split(':') for data in uncheckedPassport))

    passports = [passport for passport in passports if len(passport.keys()) == 8 or (len(passport) == 7 and 'cid' not in passport.keys())]

    return(passports)

def passportValidator(passports):
    eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validPass = 0
    
    for passport in passports:
        if (1920 <= int(passport['byr']) <= 2002
            and (2010 <= int(passport['iyr']) <= 2020)
            and (2020 <= int(passport['eyr']) <= 2030)
            and ('#' in passport['hcl'][0] and len(passport['hcl']) == 7)
            and (passport['ecl'] in eyeColors)
            and len(passport['pid']) == 9):
            if ('cm' in passport['hgt']):
                height = passport['hgt'].replace('cm','')
                if 150 <= int(height) <= 193:
                    validPass += 1 
            elif ('in' in passport['hgt']):
                height = passport['hgt'].replace('in','')
                if 59 <= int(height) <= 76:
                    validPass += 1

    return(validPass)

with open('Day4PassportInfo.txt', 'r') as passportList:
    passports = passportChecker(passportList)
    print('Part 1= ', len(passports))
    part2 = passportValidator(passports)
    print('Part 2= ', part2)