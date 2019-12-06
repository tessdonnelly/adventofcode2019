# day 5

with open("input5.txt", "r") as f:
    puzzle = f.read()

print puzzle

def TEST(puzzle):
    i = 0
    while i < len(puzzle):
        # get opcode & parameters
        instruction = "{:05d}".format(puzzle[i])
    #    print instruction
        opcode = int(instruction[3:])
        p1 = int(instruction[2])
        p2 = int(instruction[1])
        p3 = int(instruction[0])
        #print opcode
        if opcode == 99:
            print("halt!")
            return puzzle[0]
            
        if opcode == 3:
            a = input()
            puzzle[puzzle[i+1]]=a
            i+=2

        if opcode == 4:
            print puzzle[puzzle[i+1]]
            i+=2
        # check parameter 1
        if p1 > 0: a = puzzle[i+1]
        else: a = puzzle[puzzle[i+1]]

        # check parameter 2
        if p2 > 0: b = puzzle[i+2]
        else: b = puzzle[puzzle[i+2]]

        if opcode == 1:
            puzzle[puzzle[i+3]] = a+b
            i+=4

        if opcode == 2:
            puzzle[puzzle[i+3]] = a*b
            i+=4


    # print first
    return puzzle[0]

example = [1002,4,3,4,33]

with open("input5.txt", "r") as f:
    input5 = f.read()
list = [int(x) for x in input5.split(',')]

TEST(list)
