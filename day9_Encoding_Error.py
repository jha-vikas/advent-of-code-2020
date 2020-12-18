# https://adventofcode.com/2020/day/9

from typing import List

EX_INPUT = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def has_counterpart(num_list: List[int], num: int) -> bool:
    for i in range(len(num_list)):
        #print(f"i{i}")
        if ((num-num_list[i]) in num_list[(i+1):]):
            #print(num_list[(i+1):])
            return True
    return False

def first_invalid(lines: str, preamble_size: int) -> int:
    lines = lines.split("\n")
    lines = [int(i.strip()) for i in lines]
    #print(lines)

    for indx in range(preamble_size, len(lines),1):
        #print(f"indx: {indx}")
        line_split = lines[indx-preamble_size: indx]
        #print(line_split)
        num = lines[indx]
        #print(j)
        if not has_counterpart(line_split, num):
            #print(has_counterpart(line_split, num))
            return num

def window_sum_check(num_list: List[int], window: int) :
    pass


def find_cont_num(lines: str, target: int) -> int:
    lines = lines.split("\n")
    lines = [int(i.strip()) for i in lines]
    indx = lines.index(target)
    lines = lines[:(indx)]
    
    for window in range(2, len(lines),1):
        for i in range(0,len(lines)-window+1,1):
            if sum(lines[i:i+window]) == target:
                target_cont_list =  lines[i:i+window]
                return (min(target_cont_list) + max(target_cont_list))



assert first_invalid(EX_INPUT,5) == 127
assert find_cont_num(EX_INPUT, 127) == 62

with open("day9_input.txt") as f:
    INPUT = f.read().rstrip()
print(first_invalid(INPUT, 25))
print(find_cont_num(INPUT, 133015568))