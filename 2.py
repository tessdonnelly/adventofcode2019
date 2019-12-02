
# opcode 1 [1,x,y,z]
# find values from positions x and y
# place the sum of x and y in position z

# opcode 2 [2,x,y,z]
# find values from positions x and y
# place the product of x and y in position z

## opcode 99 [99,x,y,z] halts the program
import copy

def opcode(input):
    i = 0
    while i < len(input):
        if input[i] == 99:
            #print("halt!")
            break
        if input[i] == 1:
            input[input[i+3]]=(input[input[i+1]]+input[input[i+2]])
            i+=4
        if input[i] == 2:
            input[input[i+3]]=(input[input[i+1]]*input[input[i+2]])
            i+=4
    #print input
    return input[0]

## every engineer is responsible for testing her code
example = [1,9,10,3,2,3,11,0,99,30,40,50]
assert opcode(example) == 3500
assert opcode([1,0,0,0,99]) == 2
assert opcode([2,3,0,3,99]) == 2
assert opcode([2,4,4,5,99,0]) == 2
assert opcode([1,1,1,4,99,5,6,0,99])==30

## with puzzle input
# replace position 1 with value 12 and position 2 with value 2
with open("input2.txt", "r") as f:
    input2 = f.read()
list = [int(x) for x in input2.split(',')]

list1=list
list1[1]=12
list1[2]=2
print("Part 1 answer is %d" % opcode(list1))

## part 2, what inputs to position 1 and 2 give the output 19690720
for i in range(0,99):
    for j in range(0,99):
        list2 = [int(x) for x in input2.split(',')]
        list2[1]=i
        list2[2]=j
        if opcode(list2)==19690720:
            noun = i
            verb = j
            print("Noun is %d" % i)
            print("Verb is %d" % j)
            answer = i*100+j
            print("Answer is %d" % answer )
