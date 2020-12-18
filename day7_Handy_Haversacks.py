from typing import List, NamedTuple, Dict, DefaultDict, Tuple
import re
from collections import namedtuple, defaultdict

EX_INPUT = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

class Bag(NamedTuple):
    colour: str
    contains: Dict[str, int] # colour and Dict telling how many that bag contains

def line_parser(line: str) -> Bag:
    part1, part2 = line.split(" contain ")
    colour = part1[:-5]

    part2 = part2.rstrip(".")
    if part2 == "no other bags":
        return Bag(colour, {})
    
    contains = {}

    part2 = re.sub(r" bags?", "", part2)
    part2 = part2.split(", ")

    for subbags in part2:
        #count, *_ = subbags.split(" ")
        #first_space = subbags.find(" ")
        first_space = subbags.index(" ")
        count = int(subbags[:first_space].strip())
        colour2 = subbags[first_space:].strip()
        contains[colour2] = count
    return Bag(colour, contains)

def make_bags(raw: str) -> List[Bag]:
    return [line_parser(i) for i in raw.split("\n")]

# Now to check for parents
def parents(bags: List[Bag]) -> Dict[str, List[str]]:
    ic = defaultdict(list) #gives empty list if the key is not present
    for bag in bags:
        for child in bag.contains:
            ic[child].append(bag.colour)
    return ic

def can_eventually_contain(bags: List[Bag], colour: str) -> List[str]:
    parent_map = parents(bags)

    check_me = [colour]
    can_contain = set()

    while check_me:
        child = check_me.pop()
        for parent in parent_map.get(child, []):
            if parent not in can_contain:
                can_contain.add(parent)
                check_me.append(parent)
    
    return list(can_contain)

def num_bags_inside(bags: List[Bag], colour: str) -> int:
    by_colour = {bag.colour: bag for bag in bags}

    num_bags = 0
    stack: List[Tuple[str, int]] = [(colour, 1)]
    while stack:
        next_colour, multiplier = stack.pop()
        bag = by_colour[next_colour]
        for child, count in bag.contains.items():
            num_bags += multiplier * count
            stack.append((child, count * multiplier))
    return num_bags


EX_INPUT2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

BAGS1 = make_bags(EX_INPUT)
BAGS2 = make_bags(EX_INPUT2)


with open("day7_input.txt") as f:
    INPUT = f.read().rstrip()
bags = make_bags(INPUT)
print(len(can_eventually_contain(bags, 'shiny gold')))
print(num_bags_inside(bags, "shiny gold"))