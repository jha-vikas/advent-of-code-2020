# https://adventofcode.com/2020/day/16

from typing import List, NamedTuple
from collections import namedtuple
import re

EX_INPUT = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

EX_INPUT2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""


rule = namedtuple("rule", ["low", "high"]) # should use named tuple better

def input_parser(lines: str) -> List:
    rules, my_ticket, nearby_tickets = lines.split("\n\n")
    rules_str = rules.split("\n")
    rules_str = [(i.split(":")[0]).strip() for i in rules_str]
    rules = re.findall(r"[0-9]+-[0-9]+", rules)
    rules = [i.split("-") for i in rules]
    rules = [rule(int(x),int(y)) for x,y in rules]

    my_ticket = re.findall(r"[1-9]+", my_ticket)
    my_ticket = [int(x) for x in my_ticket]
    
    nearby_tickets = re.sub("^(nearby tickets:\n)","",nearby_tickets)
    nearby_tickets = nearby_tickets.split("\n")
    nearby_tickets = [list(ticket.split(",")) for ticket in nearby_tickets]
    nearby_tickets = [[int(i) for i in inner] for inner in nearby_tickets]
    return (rules_str, rules, my_ticket, nearby_tickets)

rules_str, rules, my_ticket, nearby_tickets = input_parser(EX_INPUT)

def validity_checker_num(rules: List[NamedTuple], num) -> int:
        for rule in rules:
            if rule.low <= num <= rule.high:
                return 0
        return num

def validity_checker_num2(rules: List[NamedTuple], num) -> int:
        for rule in rules:
            if not (rule.low <= num <= rule.high):
                return False
        return True

invalid_list = [[validity_checker_num(rules, i) for i in inner] for inner in nearby_tickets]
assert sum(sum(i) for i in invalid_list) == 71


def valid_filter(nearby_tickets: List[List[int]], rules:List[NamedTuple])-> List[List[int]]:
    invalid_list = [[validity_checker_num(rules, i) for i in inner] for inner in nearby_tickets]
    #assert sum(sum(i) for i in invalid_list) == 71
    index_valid_ticket = [index for index,i in enumerate(invalid_list) if sum(i) == 0]
    return [nearby_tickets[i] for i in index_valid_ticket]

rules_str, rules, my_ticket, nearby_tickets = input_parser(EX_INPUT2)

def rule_discoverer(nearby_tickets: List[List[int]], rules:List[NamedTuple], rules_str: List[str]):
    nearby_tickets = valid_filter(nearby_tickets, rules)
    nearby_tickets = list(map(list,zip(*nearby_tickets)))
    rule_map = {}

    rule_index = list(range(len(rules_str)))
    ticket_index = list(range(len(nearby_tickets)))
    while len(rule_index) > 0:
        for i in rule_index:
            rules_chunk = rules[2*i:2*(i+1)]
            rules_str_chuck = rules_str[i]
            nearby_tickets_use = [nearby_tickets[i] for i in ticket_index]
            rules_sat = [sum([validity_checker_num(rules_chunk, n) for n in inner]) for inner in nearby_tickets_use]
            if rules_sat.count(0) == 1:
                rule_index.remove(i)
                zero_ticket_index = rules_sat.index(0)
                rule_map[rules_str_chuck] = zero_ticket_index
                print(zero_ticket_index)
                ticket_index.remove(zero_ticket_index)
    
    return rule_map




if __name__ == "__main__":
    with open("day16_input.txt") as f:
        INPUT = f.read()
    INPUT = INPUT.rstrip()
    rules_str, rules, my_ticket, nearby_tickets = input_parser(INPUT)
    invalid_list = [[validity_checker_num(rules, i) for i in inner] for inner in nearby_tickets]
    print(sum(sum(i) for i in invalid_list))

    rule_map = rule_discoverer(nearby_tickets, rules, rules_str)

    departure_keys = [i for i in rule_map.keys() if i.startswith('departure')]
    print(departure_keys)

    print(sum([my_ticket[i] for i in departure_keys]))



