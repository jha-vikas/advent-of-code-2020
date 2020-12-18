# https://adventofcode.com/2020/day/5

import itertools

def row_col_calculator(code: str) -> int:
    n = len(code)
    low_num = 0
    high_num = 2**n - 1

    for i in code:
        mid = (low_num+high_num)//2
        if (i == "F") or (i == "L"):
            high_num = mid
        
        if (i == "B") or (i == "R"):
            low_num = mid + 1
    
    assert low_num == high_num
    return low_num

def seat_position(code: str):
    row = row_col_calculator(code[:7])
    col = row_col_calculator(code[7:])
    return row, col, (row*8+col)

assert seat_position("BFFFBBFRRR") == (70, 7, 567)
assert seat_position("FFFBBBFRRR") == (14, 7, 119)
assert seat_position("BBFFBBFRLL") == (102, 4, 820)

if __name__ == "__main__":
    with open("day5_input.txt") as f:
        INPUT = f.read().rstrip().split("\n")
    SEAT_IDS = [seat_position(i)[2] for i in INPUT]
    print(max(SEAT_IDS))

    SEAT_POS = [seat_position(i) for i in INPUT]

    seat_gen = list(itertools.product(range(128), range(8)))

    SEAT_IDS_POSS = [[i+1,i,i-1] for i in SEAT_IDS]
    SEAT_IDS_POSS = list(set([i for j in SEAT_IDS_POSS for i in j]))
    SEAT_IDS_POSS = [i for i in SEAT_IDS_POSS if i not in SEAT_IDS]


