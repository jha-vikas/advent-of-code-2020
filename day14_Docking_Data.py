# https://adventofcode.com/2020/day/14

import re
from typing import Dict, List
import itertools

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
            #print(i, mask)
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
    
def binary_combo(binary_str: str) -> List:
    if binary_str.find("X") == -1:
        return binary_str
    else:
        all_combs = []
        ind = binary_str.find("X")
        to_return = [(binary_str[:ind]+i+binary_str[(ind+1):]) for i in ["0","1"]]
        all_combs.extend([binary_combo(words) for words in to_return])
        return all_combs
       

def apply_mask2(mask: str, mem_loc: int):
    binary_str = bin(mem_loc)[2:]
    binary_str = binary_str.rjust(36, "0")
    binary_str = list(binary_str)

    for i, (digit , m) in enumerate(zip(binary_str, mask)):
        if m == "X" or m == "1":
            binary_str[i] = m
    binary_str = "".join(binary_str)
    #X_indices = [i for i,j in enumerate(binary_str) if j == "X"]
    all_combo = binary_combo(binary_str)
    while not all([isinstance(i, str) for i in all_combo]):
        all_combo =  list(itertools.chain(*all_combo))
    return [int(i,2) for i in all_combo]


def run2(lines: List[str]) -> int:
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
            #print(i, mask)
            mask = mask.rstrip().strip()
        elif line.startswith("mem"):
            memory, val = line.split(" = ")
            memory = int(memory[4:-1])
            new_mem_loc = apply_mask2(mask, memory)
            val = int(val.rstrip())
            for loc in new_mem_loc:
                temp_dict[loc] = val
        i += 1
    total += sum(temp_dict.values())
    temp_list.append(temp_dict)
    return total


if __name__ == "__main__":
    with open("day14_input.txt") as f:
        inp = [i.rstrip() for i in f]
    print(run(inp))
