# day 5

with open("input5.txt", "r") as f:
    puzzle = f.read()

def TEST(puzzle):
    i = 0
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
            break

        if opcode == 3:
            a = input()
            puzzle[puzzle[i+1]]=a
            i+=2

        if opcode == 4:
            # check parameter 1
            if p1 > 0: a = puzzle[i+1]
            else: a = puzzle[puzzle[i+1]]

            print a
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
        if opcode ==9:
            break

    # print first
    return puzzle[0]

example = [1002,4,3,4,33]

with open("input5.txt", "r") as f:
    input5 = f.read()
list = [int(x) for x in input5.split(',')]

test1 = [3,9,8,9,10,9,4,9,99,-1,8]
test2 = [3,9,7,9,10,9,4,9,99,-1,8]
test3 = [3,3,1108,-1,8,3,4,3,99]
test4 = [3,3,1107,-1,8,3,4,3,99]
test5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
test6 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
test7 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

TEST(list)
