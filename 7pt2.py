# day 7 refactor

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
        self.program = []
        self.output = 0
        self.inputCount=0
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
            }

    def set_program(self, program):
        self.program = program

    def set_inputs(self, inputs):
        for n in inputs:
            self.inputs.append(n)

    def set_output(self, output_computer):
        self.output_computer = output_computer

    def next_input(self):
        while self.inputCount>=len(self.inputs):
#          print "NO INPUT for", self.name
          time.sleep(.001)
        self.inputCount+=1
        return self.inputs[self.inputCount-1]

    # opcode 1
    def add(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else: x = self.program[index+1]
        if params[1] == 0:
            y = self.program[self.program[index+2]]
        else: y = self.program[index+2]
        sum = x+y
        self.program[self.program[index+3]]= sum
        return index + 4

    # opcode 2
    def mul(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else:
            x = self.program[index+1]
        if params[1] == 0:
            y = self.program[self.program[index+2]]
        else:
            y = self.program[index+2]
        product = x*y
        self.program[self.program[index+3]]= product
        return index + 4

    # opcode 3
    def inp(self, index, params):
        x = self.next_input()
        self.program[self.program[index+1]] = x
        return index + 2

    # opcode 4
    def outp(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else:
            x = self.program[index+1]
        self.output = x
        self.output_computer.set_inputs([x])
        return index + 2

    # opcode 5 - jump if TRUE
    def jit(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else:
            x = self.program[index+1]
        if params[1] == 0:
            y = self.program[self.program[index+2]]
        else:
            y = self.program[index+2]

        if x != 0:
            return y
        else:
            return index + 3

    # opcode 6 - jump if FALSE
    def jif(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else:
            x = self.program[index+1]
        if params[1] == 0:
            y = self.program[self.program[index+2]]
        else:
            y = self.program[index+2]

        if x == 0:
            return y
        else:
            return index + 3

    # opcode 7 - less than
    def lt(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else:
            x = self.program[index+1]
        if params[1] == 0:
            y = self.program[self.program[index+2]]
        else:
            y = self.program[index+2]

        if x < y:
            self.program[self.program[index+3]]= 1
        else:
            self.program[self.program[index+3]]= 0
        return index + 4

    # opcode 8 - greater than
    def eq(self, index, params):
        if params[0] == 0:
            x = self.program[self.program[index+1]]
        else:
            x = self.program[index+1]
        if params[1] == 0:
            y = self.program[self.program[index+2]]
        else:
            y = self.program[index+2]

        if x == y:
            self.program[self.program[index+3]]= 1
        else:
            self.program[self.program[index+3]]= 0
        return index + 4

    def run(self):
        index = 0
#        print self.name,': running computer'
        while True:
            code = "{:05d}".format(self.program[index])
            opcode = int(code[3:])
            #print(code)
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
    # print computer.output

# computer = Computer("TEST")

with open("input7.txt", "r") as f:
    input7 = f.read()
program = [int(x) for x in input7.split(',')]
# print program

# part 1
'''
from itertools import permutations
possibles = list(set(permutations(range(0, 5))))

maxOutput = 0
for p in possibles:
    run(program, list(p))
    if computer.output > maxOutput:
        maxOutput = computer.output

print 'Max output: {}'.format(maxOutput)

# testing for part 2
seq = [9,7,8,5,6]
program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
'''
# part 2
from itertools import permutations
possibles = list(set(permutations(range(5, 10))))

maxOutput = 0
maxPhase = []
for p in possibles:
    print p
    computerA = Computer("A")
    computerB = Computer("B")
    computerC = Computer("C")
    computerD = Computer("D")
    computerE = Computer("E")

    computerA.set_program(list(program))
    computerA.set_inputs([p[0],0])
    computerA.set_output(computerB)

    computerB.set_program(list(program))
    computerB.set_inputs([p[1]])
    computerB.set_output(computerC)

    computerC.set_program(list(program))
    computerC.set_inputs([p[2]])
    computerC.set_output(computerD)

    computerD.set_program(list(program))
    computerD.set_inputs([p[3]])
    computerD.set_output(computerE)

    computerE.set_program(list(program))
    computerE.set_inputs([p[4]])
    computerE.set_output(computerA)

    computerA.start()
    computerB.start()
    computerC.start()
    computerD.start()
    computerE.start()

    computerA.join()
    computerB.join()
    computerC.join()
    computerD.join()
    computerE.join()

    output = computerE.output

    if output > maxOutput:
        maxOutput = output
        maxPhase = p

print 'Max output: {}',maxOutput, 'from phase ',maxPhase
