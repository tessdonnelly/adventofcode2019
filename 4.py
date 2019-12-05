# day 4

# password criteria
# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease;
# they only ever increase or stay the same (like 111123 or 135679).

def password(input):
    a = [int(i) for i in str(input)]
    b = sorted(a)
    # check for increasing
    inc = None
    if ''.join([str(i) for i in a]) > ''.join([str(i) for i in b]):
        inc=False
        return
    else:
        inc=True

    # check for duplicates
    dup = None
    x = 1
    while (x<(len(a)))and(bool(dup)!=True):
        if a[x] == a[x-1]:
            dup=True
        x+=1
    if bool(inc) is True and bool(dup) is True:
        return input
    else:
        return

assert password(111111) == 111111
assert password(223450) == None
assert password(123789) == None
assert password(122345) == 122345

# part 1 answer
pws1 = []
for n in range(357253,892942+1):
    if password(n) != None:
        pws1.append(n)

print('Number of passwords 1 = %d' % len(pws1))

# part 2

def password2(input):
    a = [int(i) for i in str(input)]
    b = sorted(a)
    # check for increasing
    inc = None
    if ''.join([str(i) for i in a]) > ''.join([str(i) for i in b]):
        inc=False
        return
    else:
        inc=True

    # check for duplicates
    dup = None
    x = 1
    while (x<(len(a)))and(bool(dup)!=True):
        if a[x] == a[x-1]:
            dup=True
            print a
            print x
            while (x<len(a)-1)and (a[x]==a[x+1]):
                dup=False
                x+=1
#            if (x+2<len(a))and(a[x+1]==a[x+2]):
#                dup=False
#                print ('Dup is false again!')
#                x+=1
        x+=1
    if bool(inc) is True and bool(dup) is True:
        return input
    else:
        return

assert password2(112233) == 112233
assert password2(123444) == None
assert password2(111122) == 111122
assert password2(111111) == None


pws2 = []
for n in range(357253,(892942+1)):
    if password2(n) != None:
        pws2.append(n)

print('Number of passwords 2 = %d' % len(pws2))
