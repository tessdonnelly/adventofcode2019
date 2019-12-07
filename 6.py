# day 6

with open("input6.txt", "r") as f:
    input6 = f.readlines()

# test input = 42
test = [
'COM)B',
'B)C',
'C)D',
'D)E',
'E)F',
'B)G',
'G)H',
'D)I',
'E)J',
'J)K',
'K)L',
'K)YOU',
'I)SAN'
]

class Object():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def _add_child(self, child):
        self.children.append(child)
        return

    def getChildren(self):
        return self.children

    def getDirectOrbs(self):
        if self.parent is None: return 0
        else: return 1

# create tree
obs = {}
ob = None
i = 0
for x in input6:
    line = x.strip()
    line = line.split(')')
    orbiter = line[1]
    orbitee = line[0]

    if orbitee:
        try:
          ob1 = obs[orbitee]
        except KeyError:
          ob1 = Object(orbitee, None)
          obs[orbitee] = ob1
          #print ob1.name

    if orbiter:
        try:
          ob2 = obs[orbiter]
          ob2.parent = orbitee
        except KeyError:
          ob2 = Object(orbiter, orbitee)
          obs[orbiter] = ob2
         # print ob2.name

    ob1._add_child(orbiter)

# get total number of orbits, part 1
def getTotalOrbits(listObs):
    totalOrbs = 0
    for o in listObs:
        object = listObs[o]
        count = 0
        while object.getDirectOrbs()>0:
            count+=1
            object = listObs[object.parent]
        totalOrbs+=count
    return totalOrbs
print 'Total orbits {}'.format(getTotalOrbits(obs))

# get traversals from YOU to SAN, part 2

def getOrbits(listObs,object):
    orbits = []
    while object.getDirectOrbs()>0:
        object = listObs[object.parent]
        orbits.append(object.parent)
    orbits.remove(None)
    return orbits

def getTraversals(listObs, object1, object2):
    count = 0
    while object2 is not object1:
        object2 = listObs[object2.parent]
        count+=1
    return count

santa = obs['SAN']
me = obs['YOU']

# get my and santa's orbits
sOrbits = getOrbits(obs,santa)
mOrbits = getOrbits(obs, me)

# get my orbits
matches = list(set(sOrbits)&set(mOrbits))

# find farthest common node
max = 0
farthest = None
for x in matches:
    ob1 = obs[x]
    com = obs['COM']
    t = getTraversals(obs,com,ob1)
    if t > max:
        max = t
        farthest = x
    

# find traversals to farthest common node from YOU
meTraverse = getTraversals(obs, obs[farthest], me)-1
santaTraverse = getTraversals(obs,obs[farthest],santa)-1
totalTraversals = meTraverse+santaTraverse
print 'Traversals from Me to Santa is {}'.format(totalTraversals)
