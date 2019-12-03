## day 3

# read input3
with open('input3.txt', "r") as f:
    lines = f.readlines()
# print lines
# examples

# ex1 distance = 6
ex1 = [
'R8,U5,L5,D3',
'U7,R6,D4,L4'
]


# ex2 distance = 159
ex2 = [
'R75,D30,R83,U83,L12,D49,R71,U7,L72',
'U62,R66,U55,R34,D71,R55,D58,R83'
]

# ex3 distance = 135
ex3 = [
'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
]



def up(x,y,l,points):
    i=1
    while i <= l:
        points.append((x,y+i))
        i+=1
    return points

def down(x,y,l,points):
    i=1
    while i <= l:
        points.append((x,y-i))
        i+=1
    return points

def left(x,y,l,points):
    i=1
    while i <= l:
        points.append((x-i,y))
        i+=1
    return points

def right(x,y,l,points):
    i=1
    while i <= l:
        points.append((x+i,y))
        i+=1
    return points

def getCoords(input):
    moves = input.split(',')
    coords = []
    x = 0
    y = 0
    for m in moves:
        l = int(m[1:])
        if m[0] is 'R':
            right(x,y,l,coords)
            x+=l
        if m[0] is 'L':
            left(x,y,l,coords)
            x-=l
        if m[0] is 'U':
            up(x,y,l,coords)
            y+=l
        if m[0] is 'D':
            down(x,y,l,coords)
            y-=l
    return coords

def distance(input):
    c1 = getCoords(input[0])
    c2 = getCoords(input[1])
    matches = list(set(c1)&set(c2))
    dist=[]
    for d in list(matches):
        dist.append(abs(d[0])+abs(d[1]))
#    print dist
    return min(dist)

assert distance(ex1) == 6
assert distance(ex2) == 159
assert distance(ex3) == 135

print('Min distance is %d' % distance(lines))

def steps(input):
    c1 = getCoords(input[0])
    c2 = getCoords(input[1])
    matches = list(set(c1)&set(c2))
    steps=[]
    for m in matches:
        steps.append(c1.index(m)+c2.index(m)+2)
#    print steps
    return min(steps)

assert steps(ex1) == 30
assert steps(ex2) == 610
assert steps(ex3) ==  410

print('Min steps is %d' % steps(lines)) 
