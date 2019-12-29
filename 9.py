# day 9, we're back at it!

import collections
import itertools
import sys
import time
from threading import Thread

class Computer(Thread):
    def __init__(self, name):
    # Initialise thread.
        super(Computer, self).__init__()
        self.name = name
#       print('starting computer ', self.name)
        self.inputs = collections.deque([])
        self.program = {}
        self.output = 0
        self.inputCount=0
        self.relBase = 0
        self.output_computer = None
        self.opcodes = {
            1: self.add,
            2: self.mul,
            3: self.inp,
            4: self.outp,
            5: self.jit,
            6: self.jif,
            7: self.lt,
            8: self.eq,
            9: self.rel,
            }

    def reset(self):
        self.program.clear()
        self.inputs.clear()
        self.output = None
        self.relBase = 0

    def set_program(self, program):
        self.program.clear()
        for i in range(0, len(program)):
            self.program[i] = program[i]


    def set_inputs(self, inputs):
        for n in inputs:
            self.inputs.append(n)

    def next_input(self):
        while self.inputCount>=len(self.inputs):
#          print "NO INPUT for", self.name
          time.sleep(.001)
        self.inputCount+=1
        return self.inputs[self.inputCount-1]

    def get_value(self,index,param):
        try:
            if param == 0:
                return self.program[self.program[index]]
            elif param == 1:
                return self.program[index]
            elif param == 2:
                v = self.relBase + self.program[index]
                return self.program[v]
        except KeyError:
            return 0

    def get_output_position(self,index,param):
        try:
            if param == 0:
                return self.program[index]
            elif param == 2:
                return self.relBase + self.program[index]
        except KeyError:
            return 0

    # opcode 1
    def add(self, index, params):
        x = self.get_value(index+1, params[0])
        y = self.get_value(index+2, params[1])
        sum = x+y
        self.program[self.get_output_position(index+3, params[2])]= sum
        return index + 4

    # opcode 2
    def mul(self, index, params):
        x = self.get_value(index+1, params[0])
        y = self.get_value(index+2, params[1])
        product = x*y
        self.program[self.get_output_position(index+3, params[2])]= product
        return index + 4

    # opcode 3
    def inp(self, index, params):
        if params[0] == 2:
            x = self.next_input()
            v = self.relBase + self.program[index + 1]
            self.program[v] = x
        else:
            x = self.next_input()
            self.program[self.program[index+1]] = x
        return index + 2

    # opcode 4
    def outp(self, index, params):
        x = self.get_value(index+1, params[0])
        self.output = x
        print "output is :", x
#        self.output_computer.set_inputs([x])
        return index + 2

    # opcode 5 - jump if TRUE
    def jit(self, index, params):
        x = self.get_value(index+1, params[0])
        y = self.get_value(index+2, params[1])
        if x != 0:
            return y
        else:
            return index + 3

    # opcode 6 - jump if FALSE
    def jif(self, index, params):
        x = self.get_value(index+1, params[0])
        y = self.get_value(index+2, params[1])

        if x == 0:
            return y
        else:
            return index + 3

    # opcode 7 - less than
    def lt(self, index, params):
        x = self.get_value(index+1, params[0])
        y = self.get_value(index+2, params[1])

        if x < y:
            self.program[self.get_output_position(index+3, params[2])]= 1
        else:
            self.program[self.get_output_position(index+3, params[2])]= 0
        return index + 4

    # opcode 8 - greater than
    def eq(self, index, params):
        x = self.get_value(index+1, params[0])
        y = self.get_value(index+2, params[1])
        if x == y:
            self.program[self.get_output_position(index+3, params[2])]= 1
        else:
            self.program[self.get_output_position(index+3, params[2])]= 0
        return index + 4

    def rel(self, index, params):
        x = self.get_value(index+1, params[0])
        self.relBase = self.relBase + x
#        print "relative base is: ", self.relBase
        return index + 2

    def run(self):
        index = 0
#        print self.name,': running computer'
        while True:
            code = "{:05d}".format(self.program[index])
            opcode = int(code[3:])
#            print(code)
            params = [0,0,0]
            params[0] = int(code[2])
            params[1] = int(code[1])
            params[2] = int(code[0])
            #print(params)
            if opcode == 99:
                break
            opfunc = self.opcodes[opcode]
            index = opfunc(index,params)

def run(program, phase_seq):
  computer.output = 0
  for i in range(0, len(phase_seq)):
    computer.set_inputs([phase_seq[i], computer.output])
    computer.set_program(program)
    computer.run()


with open("input9.txt", "r") as f:
    input9 = f.read()
program = [int(x) for x in input9.split(',')]


computer = Computer("TEST")
computer.set_program(program)
computer.set_inputs([2])
computer.run()
print "output: ", computer.output
