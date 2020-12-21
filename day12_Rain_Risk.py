# https://adventofcode.com/2020/day/12

from operator import add
import math

EX_INPUT = """F10
N3
F7
R90
F11"""

class Boat:
    def __init__(self, lines: str, dirc="N", wp_loc = [0,0]):
        self.lines = lines.split("\n")
        self.loc = [0,0]
        self.directions = ["N","E","S","W"]
        self.dirc = dirc
        self.dir_index = self.directions.index(self.dirc)
        self.wp_loc = wp_loc
        #self.way_point = 

    def move(self, mov):
        if mov[0] == "F":
            mov = self.directions[self.dir_index] + mov[1:]
        
        if mov[0] in ["R", "L"]:
            turns = int(mov[1:])//90
            if mov[0] == "R":
                self.dir_index += turns
                self.dir_index = self.dir_index%4
            elif mov[0] == "L":
                self.dir_index -= turns
                self.dir_index = self.dir_index%4
        
        if mov[0] == "N":
            self.loc[0] += int(mov[1:])
        elif mov[0] == "S":
            self.loc[0] -= int(mov[1:])
        elif mov[0] == "W":
            self.loc[1] += int(mov[1:])
        elif mov[0] == "E":
            self.loc[1] -= int(mov[1:])
        
    def total_mov(self):
        for i in self.lines:
            self.move(i)
            #print(self.loc)
            #print(self.directions[self.dir_index])
        
        print(self.loc)
        print(f"Total movement: {abs(self.loc[0]) + abs(self.loc[1])}")

    def move2(self, mov):
        if mov[0] == "F":
            val = int(mov[1:])
            delta = [val*i for i in self.wp_loc]
            print(f"Delta: {delta}")
            self.loc = list( map(add, self.loc, delta) )
        
        elif mov[0] == "N":
            self.wp_loc[0] += int(mov[1:])
        
        elif mov[0] == "S":
            self.wp_loc[0] -= int(mov[1:])

        elif mov[0] == "E":
            self.wp_loc[1] += int(mov[1:])
        
        elif mov[0] == "W":
            self.wp_loc[1] -= int(mov[1:])
        
        elif mov[0] in ["R", "L"]:
            if mov[0] == "R":
                sign = -1
            if mov[0] == "L":
                sign = 1
            angle = math.radians(sign*int(mov[1:])%360)
            y = self.wp_loc[0]
            x = self.wp_loc[1]

            self.wp_loc[0] = x*math.sin(angle) + y*math.cos(angle)
            self.wp_loc[1] = x*math.cos(angle) - y*math.sin(angle)
            
    def total_mov2(self):
        for i in self.lines:
            self.move2(i)
        
        print(self.loc)
        print(f"Total movement: {round(abs(self.loc[0]) + abs(self.loc[1]))}")




eg = Boat(EX_INPUT, dirc="E")
eg.total_mov()

eg2 = Boat(EX_INPUT, dirc="E", wp_loc=[1,10])
eg2.total_mov2()



if __name__ == "__main__":
    with open("day12_input.txt") as f:
        INPUT = f.read().rstrip()
    test = Boat(INPUT, dirc = "E")
    test.total_mov()

    test2 = Boat(INPUT, dirc = "E", wp_loc=[1,10])
    test2.total_mov2()


