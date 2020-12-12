# day1
# https://adventofcode.com/2020/day/1

from typing import List, Tuple
from itertools import combinations

EX_INPUT = """1721
979
366
299
675
1456"""

def to_list(input: str) -> List[int]:
    return [int(x) for x in input.split("\n")]

assert(len(to_list(EX_INPUT))) == 6

def generate_combinations(input: List[int], r) -> List[Tuple]:
    return combinations(input, r)

assert(len(list(generate_combinations(to_list(EX_INPUT),2)))) == 15

def find_multiplication2(comb: List[Tuple], val: int) -> int:
    required_tuple = [i for i in comb if sum(i) == val]
    required_tuple = required_tuple[0]
    return required_tuple[0]*required_tuple[1]

def find_multiplication3(comb: List[Tuple], val: int) -> int:
    required_tuple = [i for i in comb if sum(i) == val]
    required_tuple = required_tuple[0]
    return required_tuple[0]*required_tuple[1]*required_tuple[2]

with open("day1_input.txt") as f:
    INPUT = [int(line.strip()) for line in f]


if __name__ == "__main__":
    #my_list = to_list(EX_INPUT)
    my_list = INPUT
    my_comb = generate_combinations(my_list, 2)
    print(find_multiplication2(my_comb, 2020))
    my_comb = generate_combinations(my_list, 3)
    print(find_multiplication3(my_comb, 2020))


