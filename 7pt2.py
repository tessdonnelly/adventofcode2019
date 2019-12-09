# day 7
# day 5

with open("input5.txt", "r") as f:
    puzzle = f.read()

def TEST(puzzle,inputList,outputList):
    i = 0
    inputCount=0
    while i < len(puzzle):
        # get opcode & parameters
        instruction = "{:05d}".format(puzzle[i])
        #print instruction
        opcode = int(instruction[3:])
        p1 = int(instruction[2])
        p2 = int(instruction[1])
        p3 = int(instruction[0])
        #print opcode

        if opcode == 99:
            print("halt!")
            return output

        if opcode == 3:
            if inputCount>=len(inputList):
                print('Oh no! no input!')
                break
            else:
                a = inputList[inputCount]
                inputCount+=1
                print 'Input: {}'.format(a)
                puzzle[puzzle[i+1]]=a
                i+=2

        if opcode == 4:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else: a = puzzle[puzzle[i+1]]
            print 'Output: {}'.format(a)
            outputList.append(a)
            output = a
            i+=2

        if opcode == 1:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else: a = puzzle[puzzle[i+1]]
            # check parameter 2
            if p2 > 0: b = puzzle[i+2]
            else: b = puzzle[puzzle[i+2]]

            puzzle[puzzle[i+3]] = a+b
            i+=4

        if opcode == 2:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else:a = puzzle[puzzle[i+1]]
            # check parameter 2
            if p2 > 0: b = puzzle[i+2]
            else: b = puzzle[puzzle[i+2]]

            puzzle[puzzle[i+3]] = a*b
            i+=4

        # jump-if-true
        # if the first parameter is non-zero,
        # it sets the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing
        if opcode == 5:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else:a = puzzle[puzzle[i+1]]
            # check parameter 2
            if p2 > 0: b = puzzle[i+2]
            else: b = puzzle[puzzle[i+2]]

            if a>0: i = b
            else: i+=3
        # jump-if-false
        # if the first parameter is zero,
        # it sets the instruction pointer to the value from the second parameter.
        # Otherwise, it does nothing.
        if opcode == 6:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else:a = puzzle[puzzle[i+1]]
            # check parameter 2
            if p2 > 0: b = puzzle[i+2]
            else: b = puzzle[puzzle[i+2]]

            if a==0: i = b
            else: i+=3
        # less than:
        # if the first parameter is less than the second parameter,
        # it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        if opcode == 7:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else:a = puzzle[puzzle[i+1]]
            # check parameter 2
            if p2 > 0: b = puzzle[i+2]
            else: b = puzzle[puzzle[i+2]]

            if a<b: puzzle[puzzle[i+3]]=1
            else: puzzle[puzzle[i+3]]=0
            i+=4
        # equals:
        # if the first parameter is equal to the second parameter,
        # it stores 1 in the position given by the third parameter.
        # Otherwise, it stores 0.
        if opcode == 8:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else:a = puzzle[puzzle[i+1]]
            # check parameter 2
            if p2 > 0: b = puzzle[i+2]
            else: b = puzzle[puzzle[i+2]]

            if a==b: puzzle[puzzle[i+3]]=1
            else: puzzle[puzzle[i+3]]=0
            i+=4

    # print first
    return output

with open("input7.txt", "r") as f:
    input7 = f.read()
inputs = [int(x) for x in input7.split(',')]

from itertools import permutations
possibles = list(set(permutations(range(5, 10))))

maxOutput = 0
# for p in possibles:
    #print list(p)

    #phase = list(p)

aList = []
bList = []
cList = []
dList = []
eList = []

phase = [9,8,7,6,5]
aList.append(phase[0])
bList.append(phase[1])
cList.append(phase[2])
dList.append(phase[3])
eList.append(phase[4])

aList.append(0)
TEST(inputs,aList,bList)
TEST(inputs,bList,cList)
TEST(inputs,cList,dList)
TEST(inputs,dList,eList)
output = TEST(inputs,eList,aList)

# output = TEST(inputs, e1,e2)
#    if output > maxOutput:
#        maxOutput = output

# print 'Max output: {}'.format(maxOutput)
