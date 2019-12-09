# day 8
with open("input8.txt", "r") as f:
    line = f.read()

input8 = line.strip()
i = 0
width = 25
height = 6
count = 0
layers = []
while i<len(input8):
    layer = []
    layers.append(layer)
    row = 0
    while row < height:
        rWidth = i + width
        layer.append([])
        while i < rWidth:
            layer[row].append(input8[i])
            i+=1
        row+=1

def countNums(inL,num):
    count = 0
    for y in inL:
        for x in y:
            if x is num:
                count +=1
    return count

minZeros = countNums(layers[0],'0')
zeroLayer = layers[0]
j = 1
while j < len(layers):
    zero = countNums(layers[j],'0')
    if zero < minZeros:
        minZeros = zero
        zeroLayer = layers[j]
    j+=1

product = countNums(zeroLayer,'1')*countNums(zeroLayer,'2')
print 'product of 1s and 2s is {}'.format(product)

## part 2
image = []
a = 0
while a < height:
    image.append([])
    b = 0
    while b < width:
        image[a].append('2')
        b+=1
    a+=1


for l in layers:
    if countNums(image,'2') == 0:
        break
    row = 0
    while row < 6:
        i = 0
        while i < 25:
            if image[row][i] == '2' and l[row][i] !='2':
                image[row][i]=l[row][i]
            i+=1
        row+=1


print image
