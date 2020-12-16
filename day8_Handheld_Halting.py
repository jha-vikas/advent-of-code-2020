# https://adventofcode.com/2020/day/8

from typing import List

EX_INPUT = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

class Position:
    def __init__(self, code_series):
        self.code_series = code_series
        self.val = 0
        self.old_val = 0
        self.pos = 0
        self.pos_done = []
    
    #def code_series_splitter(self):
    #    code_list = self.code_series.split("\n")

    def processor(self, code: List):
        act, size =  code
        size = int(size)
        
        if act == "nop":
            self.pos += 1
            self.old_val = self.val
        
        if act == "acc":
            self.old_val = self.val
            self.val += size
            self.pos += 1
        
        if act == "jmp":
            self.pos += size
            self.old_val = self.val

    def mover(self):
        self.codes = self.code_series.split("\n")
        act_val_0 = [s.split(" ") for s in self.codes]
        #print(self.codes)
        while True:
            if self.pos > len(self.codes):
                print("Program terminated successfully")
                break
            code = act_val_0[self.pos]
            #print(code)
            self.processor(code)
            #print(self.old_val, self.val)
            if self.pos in self.pos_done:
                print(self.old_val)
                #print(self.codes[self.pos])
                break
            else:
                self.pos_done.append(self.pos)
    
    def mover2(self):
        self.val = 0
        self.old_val = 0
        self.pos = 0
        self.pos_done = []
        #print(self.codes)
        while True:
            if self.pos >= len(self.act_val1):
                print("Program terminated successfully")
                print(f"old value: {self.old_val}")
                print(f"value: {self.val}")
                flag = True
                break
            code = self.act_val1[self.pos]
            #print(code)
            self.processor(code)
            #print(self.old_val, self.val)
            if self.pos in self.pos_done:
                print(self.old_val)
                #print(self.codes[self.pos])
                flag = False
                break
            else:
                self.pos_done.append(self.pos)
        print(flag)
        return flag


    def repairer(self):
        self.codes = self.code_series.split("\n")
        self.act_val = [tuple(s.split(" ")) for s in self.codes]
        for i in range(len(self.act_val)):
            print(f"i:{i}")
            act, _ =  self.act_val[i]
            if act == "jmp" or act == "nop":
                self.act_val1 = [list(i) for i in self.act_val]
                if act == "jmp":
                    self.act_val1[i][0] = "nop"
                    #print(self.act_val1)
                elif act == "nop":                    
                    self.act_val1[i][0] = "jmp"
                    #print(self.act_val1)

                if self.mover2():
                    print(f"old_val:{self.old_val}")
                    break
            
            else:
                continue
                




#example = Position(EX_INPUT)
#example.mover()
#example.repairer()

with open("day8_input.txt") as f:
    INPUT = f.read().rstrip()
problem1 = Position(INPUT)
problem1.mover()
problem1.repairer()
        
        
            



