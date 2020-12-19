# https://adventofcode.com/2020/day/10

from typing import List, Dict
from collections import Counter

EX_INPUT = """16
10
15
5
1
11
7
19
6
12
4"""

EX_INPUT2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def parse_lines(lines: str) -> List[int]:
    lines = lines.rstrip().split("\n")
    lines = [int(i) for i in lines]
    lines = [0] + lines + [max(lines) + 3]
    lines.sort()
    return lines

def jolt_counter(lines: List[int]):
    counts = [(lines[i+1]-lines[i]) for i in range(len(lines)-1)]
    return Counter(counts)


def path_counter(lines: List[int]) -> int:
    op = lines[-1]  #the final output

    # num_path[i] is the number of paths to i
    num_path = [0] * (op + 1)

    num_path[0] = 1 #Only one way to get to input socket

    if 1 in lines:
        num_path[1] = 1
    
    if 2 in lines and 1 in lines:
        num_path[2] = 2
    elif 2 in lines:
        num_path[2] = 1
    
    for i in range(3, op+1):
        if i not in lines:
            continue

        num_path[i] = num_path[i-3] + num_path[i-2] + num_path[i-1]
    
    return num_path[op]


lines = parse_lines(EX_INPUT)
print(jolt_counter(lines))
assert path_counter(lines) == 8

lines = parse_lines(EX_INPUT2)
print(jolt_counter(lines))
assert path_counter(lines) == 19208


if __name__ == "__main__":
    with open("day10_input.txt") as f:
        INPUT = f.read().rstrip()
    lines = parse_lines(INPUT)
    counts = jolt_counter(lines)
    print(counts[1]*counts[3])
    print(path_counter(lines))

