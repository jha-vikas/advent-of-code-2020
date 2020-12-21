# https://adventofcode.com/2020/day/11

from typing import List, Tuple, Dict
import itertools
from collections import defaultdict, Counter

EX_INPUT = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


#If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.




def create_state(lines: str) -> Dict:
    #state = defaultdict("0")
    state = {}
    lines = lines.split("\n")
    rows, cols = len(lines), len(lines[0])

    for i in range(rows):
        for j in range(cols):
            state[(i,j)] = lines[i][j]
    return rows, cols, state


class State:
    def __init__(self, lines: str):
        self.lines = lines
        self.state = {}
        self.next_state = {}
        self.next_state2 = {}
        self.count = 0
        self.count2 = 0
        self.directions = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
    
    def create_state(self):
        #state = defaultdict("0")
        self.lines = self.lines.split("\n")
        self.rows, self.cols = len(self.lines), len(self.lines[0])

        for i in range(self.rows):
            for j in range(self.cols):
                self.state[(i,j)] = self.lines[i][j]
    
    def adjacent_seats(self, loc: Tuple[int]) -> List[Tuple[int]]:
        row,col = loc
        row_min = max(row-1, 0)
        col_min = max(col-1, 0)
        row_max = min(row+2, self.rows)
        col_max = min(col+2, self.cols)
        #print(row_min, row_max, col_min, col_max)
        adj_seats = list(itertools.product((range(row_min, row_max)), (range(col_min, col_max))))
        adj_seats.remove(tuple(loc))
        return adj_seats

    def next_state_creater(self) -> Dict:
        for key in self.state.keys():
            adj_seats = self.adjacent_seats(key)
            occ       = [self.state[i] for i in adj_seats]
            
            if (self.state[key] == "L") and (occ.count("#") == 0):
                self.next_state[key] = "#"
            elif (self.state[key] == "#") and (occ.count("#") >= 4):
                self.next_state[key] = "L"
            elif self.state[key] == ".":
                self.next_state[key] = "."
            else:
                self.next_state[key] = self.state[key]
        
        if self.state == self.next_state:
            print("Stable configuation reached")
            print(self.count)
            return True
        else:
            self.state = self.next_state
            self.next_state = {}
            self.count = self.count + 1


    
    def first_seen(self, loc: Tuple[int], direction: Tuple[int]) -> str:
        n_row, n_col =loc
        r,c     = direction

        while True:
            n_row = n_row + r
            n_col = n_col + c
        
            if (0 <= n_row < self.rows) and (0 <= n_col < self.cols):
                nb = self.state[n_row, n_col]
                if nb == "#" or nb == "L":
                    return nb
            else:
                return "."


    def next_state_step2(self, loc: Tuple[int]) -> str:
        counts = Counter(self.first_seen(loc, direction) for direction in self.directions)
        nb = self.state[loc]
        if nb == 'L' and counts['#'] == 0:
            return '#'
        if nb == '#' and counts['#'] >= 5:
            return 'L'
        else:
            return nb
    
    def next_state_creater2(self) -> Dict:
        for key in self.state.keys():
            self.next_state2[key] = self.next_state_step2(key)
        

        if self.state == self.next_state2:
            print("Stable configuation reached for stage 2")
            print(self.count2)
            return True
        else:
            self.state = self.next_state2
            self.next_state2 = {}
            self.count2 = self.count2 + 1



st = State(EX_INPUT)
st.create_state()

while True:
    if st.next_state_creater():
        break

RESULT_TEST = """#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""


result_state = State(RESULT_TEST)
result_state.create_state()
assert result_state.state == st.state

st = State(EX_INPUT)
st.create_state()

while True:
    if st.next_state_creater2():
        break

RESULT_TEST2 = """#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""

result_state2 = State(RESULT_TEST2)
result_state2.create_state()
assert result_state2.state == st.state


#five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). 
# The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, 
# and floor never changes.




if __name__ == "__main__":
    with open("day11_input.txt") as f:
        INPUT = f.read().rstrip()
        test = State(INPUT)
        test.create_state()

        test2 = State(INPUT)
        test2.create_state()
    
    while True:
        if test.next_state_creater():
            break
    print(f"Count of occupied for part1: {list(test.state.values()).count('#')}")

    while True:
        if test2.next_state_creater2():
            break
    print(f"Count of occupied for part2: {list(test2.state.values()).count('#')}")