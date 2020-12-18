# https://adventofcode.com/2020/day/3

from typing import List

EX_INPUT = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

def pattern_point_returner(pattern: str, n: int) -> str:
    """return the pattern (tree or open space) at n point"""
    m = len(pattern)
    return pattern[(n%m)-1]


def tree_counter(IP: List[str], r: int=3, d: int=1) -> int:

    IP = [j for i,j in enumerate(IP) if (i%d == 0)]
    pattern_followed = [pattern_point_returner(j,(r*i)+1) for i,j in enumerate(IP)]
    print(pattern_followed)
    tree_count = sum([1 for i in pattern_followed if i == '#'])
    return tree_count

#assert(tree_counter(EX_INPUT) == 7)
assert(tree_counter(EX_INPUT.split('\n'), r=1, d=1) == 2)
assert(tree_counter(EX_INPUT.split('\n'), r=3, d=1) == 7)
assert(tree_counter(EX_INPUT.split('\n'), r=5, d=1) == 3)
assert(tree_counter(EX_INPUT.split('\n'), r=7, d=1) == 4)
assert(tree_counter(EX_INPUT.split('\n'), r=1, d=2) == 2)


if __name__ == "__main__":
    with open("day3_input.txt") as f:
        INPUT = [line.rstrip() for line in f]
    
    print(tree_counter(INPUT, r=1, d=1) * tree_counter(INPUT, r=3, d=1) * tree_counter(INPUT, r=5, d=1) * 
            tree_counter(INPUT, r=7, d=1) * tree_counter(INPUT, r=1, d=2))
