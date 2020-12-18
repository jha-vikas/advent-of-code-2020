# https://adventofcode.com/2020/day/4

from typing import List
import re

EX_INPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

#fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


#EX_INPUT.split('\n\n')

with open('day4_input.txt') as f:
    NEW_INPUT = f.read().split('\n\n')

def is_valid(passport: str) -> bool:
    return len([i for i in fields if (i not in passport)]) == 0

def is_valid2(passport: str) -> bool:
    if len([i for i in fields if (i not in passport)]) > 0:
        return False
    passport = re.split(r" |\n", passport)
    passport = dict([i.split(":") for i in passport])

    #print("level1")

    try:
        passport['byr'] = int(passport['byr'])
        passport['iyr'] = int(passport['iyr'])
        passport['eyr'] = int(passport['eyr'])
    except:
        return False
    
    #print("level2")

    try:
        hgt = int(re.match(r"[0-9]+", passport['hgt'])[0])
    except:
        return False
    
    #print("level3")

    if (passport['byr'] < 1920) or (passport['byr'] > 2002):
        return False
    if (passport['iyr'] < 2010) or (passport['iyr'] > 2020):
        return False
    if (passport['eyr'] < 2020) or (passport['eyr'] > 2030):
        return False
    

    if "cm" in passport['hgt']:
        if (hgt < 150) or (hgt > 193):
            return False
    elif "in" in passport['hgt']:
        if (hgt < 59) or (hgt > 76):
            return False
    else:
        return False

    if len(re.findall(r"\#[0-9a-f]+", passport['hcl'])) == 0:
        return False

    if len(re.findall(r"\#[0-9a-f]+", passport['hcl'])[0]) != 7:
        return False
    
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    
    if len(re.findall(r"[0-9]{9}", passport['pid'])) == 0:
        return False
    
    if re.findall(r"[0-9]{9}", passport['pid'])[0] != passport['pid']:
        return False
    
    return True
    
    

if __name__ == "__main__":
    with open('day4_input.txt') as f:
        NEW_INPUT = f.read().split('\n\n')
    NEW_INPUT =  [i.rstrip() for i in NEW_INPUT]
    #counts = sum([is_valid(i) for i in NEW_INPUT])
    counts = sum([is_valid2(i) for i in NEW_INPUT])
    print(counts)