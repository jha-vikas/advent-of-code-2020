# https://adventofcode.com/2020/day/17

from typing import List, NamedTuple, Tuple, Iterator, Set
from collections import namedtuple, Counter
import itertools

EX_INPUT = """.#.
..#
###"""

Point = Tuple[int,...]


def neighbours(point: Point) -> Iterator[Point]:
    dim = len(point)
    changes = [[-1,0,1] for _ in range(dim)]
    for deltas in itertools.product(*changes):
        if any(d != 0 for d in deltas):
            p: List[int] = [x + dx for x, dx in zip(point, deltas)]
            yield tuple(p)

State = Set[Point]

def change_state(state: State) -> State:
    new_points = {
        p
        for point in state
        for p in neighbours(point)
        if p not in state
    }

    next_state = set()

    for point in state:
        n = sum(p in state for p in neighbours(point))
        if n in (2,3): # use tuple as it faster
            next_state.add(point)
    
    for point in new_points:
        n = sum(p in state for p in neighbours(point))
        if n == 3:
            next_state.add(point)
    
    return next_state

def create_state(lines: str, dim: int) -> State:
    lines = lines.rstrip().split("\n")
    pad = tuple([0] * (dim-2))
    return {
        (x,y) + pad
        for y, row in enumerate(lines)
        for x, c in enumerate(row)
        if c == "#"
    }


state3 = create_state(EX_INPUT, 3)

for _ in range(6):
    state3 = change_state(state3)

assert len(state3) == 112

state4 = create_state(EX_INPUT, 4)

for _ in range(6):
    state4 = change_state(state4)

assert len(state4) == 848


if __name__ == "__main__":
    with open("day17_input.txt") as f:
        INPUT = f.read()
    state_3 = create_state(INPUT, 3)
    for _ in range(6):
        state_3 = change_state(state_3)
    print(len(state_3))

    state_4 = create_state(INPUT, 4)
    for _ in range(6):
        state_4 = change_state(state_4)
    print(len(state_4))