# https://adventofcode.com/2020/day/15

from typing import List
from collections import defaultdict
import itertools

EX_INPUT = [0,3,6]

"""
def next_num(input: List[int], turns: int) -> int:
    # Does not work
    turn_count = {}
    n = len(input)
    n_shout = 0

    for turn in range(1, turns+1):
        if turn <= n:
            num = input[turn-1]
            turn_count[num] = turn
            n_shout = num
        elif turn > n:
            if turn_count[n_shout] == 0:
                turn_count[n_shout] = turn
                turn_count[0] = turn
                n_shout = 0
            else:
                n_shout = turn - turn_count[n_shout]
                turn_count[n_shout] = turn
        print(n_shout)
        #print(turn_count)
    return n_shout
"""
        
def spoken_num(ip: List[int]) -> int:
    turn_count = {} # when was the last time the num was spoken
    n = len(ip)
    n_spoken: int
    diff = None

    for i in itertools.count(0):
        if i < n:
            # initial numbers
            n_spoken = ip[i]
        elif diff:
            # seen before. Use the diff between current & prebious seen
            n_spoken = diff
        else:
            # num seen frst time
            n_spoken = 0
        
        if n_spoken in turn_count:
            # check the diff
            diff = i - turn_count[n_spoken]
        else:
            # first visit, so no diff. Making diff none again
            diff = None
        
        # update the turn_count dict
        turn_count[n_spoken] = i
        yield n_spoken

def run(ip: List[int], turns: int) -> int:
    num_shouted = spoken_num(ip)
    for i in range(turns):
        num = next(num_shouted)
        if i % 1000 == 0:
            print(i, round(i / turns,2),"%")
    return num

assert run([0,3,6],10) == 0
assert run([1,3,2],2020) == 1
assert run([2,1,3],2020) == 10
assert run([1,2,3],2020) == 27
assert run([2,3,1],2020) == 78
assert run([3,2,1],2020) == 438
assert run([3,1,2],2020) == 1836

INPUT = [0,12,6,13,20,1,17]
print(run(INPUT, 2020))

#assert run([0,3,6],30000000) == 175594

print(run(INPUT, 30000000))