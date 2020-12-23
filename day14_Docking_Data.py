# https://adventofcode.com/2020/day/14

import re
from typing import Dict, List

EX_INPUT = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

# To fill the 0s:  '{:0>36}'.format(bit_value) or bit_value.rjust(36, "0")



def line_parser(lines: str) -> List[Dict]:
    lines = lines.rstrip().split("\n")
    return lines
    


def apply_mask(mask: str, n:int) -> int:
    binary_str = bin(n)[2:]
    binary_str = binary_str.rjust(36, "0")
    binary_str = list(binary_str)
    for i, (digit , m) in enumerate(zip(binary_str, mask)):
        if m == "0" or m == "1":
            binary_str[i] = m
    binary_str = "".join(binary_str)
    return int(binary_str,2)


def run(lines: List[str]) -> int:
    total = 0
    mask  = None
    temp_list = []
    temp_dict = {}
    i = 0
    for line in lines:
        if line.startswith("mask"):
            #total += sum(temp_dict.values())
            #temp_list.append(temp_dict)
            #temp_dict = {}
            _, mask = line.split(" = ")
            print(i, mask)
            mask = mask.rstrip().strip()
        elif line.startswith("mem"):
            memory, val = line.split(" = ")
            memory = memory[4:-1]
            val = int(val.rstrip())
            temp_dict[memory] = apply_mask(mask, val)
        i += 1
    total += sum(temp_dict.values())
    temp_list.append(temp_dict)
    return total
    

if __name__ == "__main__":
    with open("day14_input.txt") as f:
        inp = [i.rstrip() for i in f]
    print(run(inp))
