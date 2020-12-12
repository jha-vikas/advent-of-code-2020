# https://adventofcode.com/2020/day/2

import re

EX_INPUT = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""

def is_valid(rule_password: str) -> bool:
    rule, password     = rule_password.split(": ")
    upper_lower, ip    = rule.split(" ")
    lower, upper       = [int(i) for i in upper_lower.split("-")]
    counts             = password.count(ip)
    return ((counts <= upper) and (counts >= lower))

assert is_valid("1-3 a: abcde") == True
assert is_valid("1-3 b: cdefg") == False
assert is_valid("2-9 c: ccccccccc") == True

#Correct_pass_count = sum([is_valid(i) for i in EX_INPUT.split('\n')])
#print(f"Correct password count for example is: {Correct_pass_count}")

def is_valid2(rule_password: str) -> bool:
    rule, password     = rule_password.split(": ")
    upper_lower, ip    = rule.split(" ")
    lower, upper       = [(int(i)-1) for i in upper_lower.split("-")]
    return not ((ip == password[lower]) == (ip == password[upper]))

assert is_valid2("1-3 a: abcde") == True
assert is_valid2("1-3 b: cdefg") == False
assert is_valid2("2-9 c: ccccccccc") == False

    



if __name__ == "__main__":
    with open("day2_input.txt") as f:
        password_list = [line.strip() for line in f]
    #print(password_list)
    #Correct_pass_count = sum([is_valid(i) for i in password_list])
    Correct_pass_count = sum([is_valid2(i) for i in password_list])
    print(f"Correct password count for example is: {Correct_pass_count}")