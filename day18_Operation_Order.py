import re
from typing import Callable

ptn = r"\([^\(]+?\)"

def solve(l: str) -> int:
    #num_ptn = r"^[^{ *+()}]+"
    a = re.search(r"^[^{ *+()}]+", l)
    total = int(a.group())
    l = l[a.span()[1]:]

    while len(l) > 0:
        s = re.search(r"^[{ *+()}]+", l)
        symb = s.group()
        l = l[s.span()[1]:]
        a = re.search(r"^[^{ *+()}]+", l)
        num = int(a.group())
        l = l[a.span()[1]:]
        
        if symb == "+":
            total = total + num
        elif symb == "*":
            total = total * num
    return total


def solve2(l: str) -> int:
    add_ptn = r"(([0-9]+\+)+[0-9]+)"
    while len(re.findall(add_ptn, l)) > 0:
        cl2 = [(x.group(),x.span()) for x in re.finditer(add_ptn,l)]
        vals2 = [(str(solve(i)), len(i), i) for i,_ in cl2]
        for val,length,txt in vals2:
            loc1 = l.find(txt)
            loc2 = loc1 + length
            l = l[:loc1] + val + l[loc2:]
    
    soln = str(solve(l))
    return soln


def solver(line: str, solver_func: Callable) -> int:
    line = re.sub(" +","",line)
    while len(re.findall(ptn, line)) > 0:
        cl = [(x.group(),x.span()) for x in re.finditer(ptn,line)]
        vals = [(str(solver_func(i[1:-1])), len(i), i) for i,_ in cl]

        for val,length,txt in vals:
            loc1 = line.find(txt)
            loc2 = loc1 + length
            line = line[:loc1] + val + line[loc2:]
    soln = int(solver_func(line))

    return soln



assert solver("1 + 2 * 3 + 4 * 5 + 6", solve) == 71
assert solver("2 * 3 + (4 * 5)", solve) == 26
assert solver("5 + (8 * 3 + 9 + 3 * 4 * 3)", solve) == 437
assert solver("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", solve) == 12240
assert solver("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", solve) == 13632

assert solver("1 + 2 * 3 + 4 * 5 + 6", solve2) == 231
assert solver("2 * 3 + (4 * 5)", solve2) == 46
assert solver("5 + (8 * 3 + 9 + 3 * 4 * 3)", solve2) == 1445
assert solver("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", solve2) == 669060
assert solver("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", solve2) == 23340

with open("day18_input.txt") as f:
    INPUT = f.read()
INPUT = INPUT.rstrip().split("\n")

solns1 = [solver(txt, solve) for txt in INPUT]
print(sum(solns1))

solns2 = [solver(txt, solve2) for txt in INPUT]
print(sum(solns2))

