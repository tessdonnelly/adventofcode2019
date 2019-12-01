
import math

with open("input1.txt", "r") as f:
    lines = f.readlines()

# lines = [
# "12",
# "14",
# "1969",
# "100756"
# ]
#sum = 0

## part 1
# for line in lines:
#    mass = int(line)
#    modfuel = int(math.floor((mass/3))-2)
#    sum += modfuel

# print sum

## part 2

def fuel(mass, modsum):
    if mass>6:
        newfuel = int(math.floor((mass/3))-2)
        modsum+=newfuel
        return fuel(newfuel,modsum)
    return modsum

totalsum = 0
for line in lines:
    totalsum += fuel(int(line),0)

print("Total is %d" % totalsum)
