# https://adventofcode.com/2020/day/13

from typing import List
import time
from math import gcd

EX_INPUT = """939
7,13,x,x,59,x,31,19"""


def next_bus(ticket: str) -> int:
    ticket = ticket.rstrip()
    earliest, buses = ticket.split("\n")
    earliest = int(earliest.rstrip())
    buses = buses.rstrip()
    buses = buses.replace("x,","")
    buses = buses.replace(",x","")
    buses = [int(i) for i in buses.split(",")]

    wt_time = earliest
    right_bus = 0

    for i in buses:
        if earliest % i == 0:
            return 0
        else:
            if wt_time > (i - (earliest % i)):
                #print(i, wt_time, (i - (earliest % i))
                wt_time = (i - (earliest % i))
                right_bus = i
    
    return right_bus*wt_time




def line_parser(lines: str) -> List[List[int]]:
    _, lines  = lines.rstrip().split("\n")
    lines     = lines.split(",")
    lines     = [i.strip() for i in lines]
    num_indices = [i for i,j in enumerate(lines) if j != "x"]
    offsets   = list(range(len(lines)))
    lines     = [int(lines[i]) for i in num_indices]
    offsets   = [offsets[i] for i in num_indices]
    return lines, offsets


"""
def lcm(l:List[int]):
    lcm1 = l[0]
    for i in l[1:]:
        lcm1 = lcm1*i//gcd(lcm, i)
    return lcm1
"""

def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(l:List[int]):
    lcm1 = l[0]
    for i in l[1:]:
        lcm1 = lcm1*i//compute_gcd(lcm1, i)
    return lcm1


def lowest_LCM_offset2(l:List[int], o:List[int]) -> List[int]:
    val_offset_pairs = list(zip(l,o))
    val_off_diff     = [x-y for x,y in val_offset_pairs]
    greater          = max(val_off_diff)
    #incr             = l[val_off_diff.index(greater)]
    
    i = 0
    t1 = time.time()
    l2 = [l[0]]
    #n2 = [l[0]]  #initiate
    o2 = [o[0]]
    greater = l[0]

    for i in range(1,len(l)):
        incr = lcm(l2)
        l2.append(l[i])
        o2.append(o[i])
        print(i, l2, incr)
        #incr = lcm(l2)
        val_offset_pairs2 = list(zip(l2,o2))
        print(val_offset_pairs2)
        #val_off_diff2    = [x-y for x,y in val_offset_pairs2]
        print(greater)

        while True:
            rm_list = [(greater+off)%val for val,off in val_offset_pairs2]
            if all(rm == 0 for rm in rm_list):
                lcm_o = greater
                print(lcm_o)
                break
            greater += incr
            if i % 1000 == 0:
                print(i, time.time() - t1)
            i += 1

            #print(greater)
            #if greater // 1_000_000 == 0:
            #    print(time.time() - t1, greater)
        print(lcm_o)
     
    
assert next_bus(EX_INPUT) == 295

if __name__ == "__main__":
    with open("day13_input.txt") as f:
        INPUT = f.read()
    print(next_bus(INPUT))
    num_off = line_parser(INPUT)
    L       = num_off[0] #[x for x in sorted(num_off[0])]
    O       = num_off[1] #[x for _,x in sorted(zip(num_off[0],num_off[1]))]

    lowest_LCM_offset2(L, O)


