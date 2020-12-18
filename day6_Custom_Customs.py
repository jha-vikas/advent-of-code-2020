# https://adventofcode.com/2020/day/6

from typing import List, Set

EX_INPUT = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def len_counter(input: str) -> int:
    input = input.rstrip().split("\n\n")
    input = [i.replace("\n", '') for i in input]
    return sum([len(set(i)) for i in input])

def list_maker(input: str) -> List[List[str]]:
    input = input.rstrip().split("\n\n")
    input = [i.split("\n") for i in input]
    return input

def common_letter_len(input_list: List[str]) -> str:
    d = [list(i) for i in input_list]
    return len(set(d[0]).intersection(*d))


assert len_counter(EX_INPUT) == 11

assert sum([common_letter_len(i) for i in list_maker(EX_INPUT)]) == 6

if __name__ == "__main__":
    with open("day6_input.txt") as f:
        INPUT = f.read()
    print(len_counter(INPUT))
    print(sum([common_letter_len(i) for i in list_maker(INPUT)]))