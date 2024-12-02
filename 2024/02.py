import re
import numpy

f = open("02input.txt",'r')

data = f.readlines()

'''
data = ["7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"]
'''

total = 0
total2 = 0

def checkone(a):
    b = sorted(a)
    c = sorted(a,reverse=True)
    if a == b:
        this = a[0]
        for j in a[1:]:
            if j == this or j > this + 3:
                return False
            this = j
    elif a == c:
        this = a[0]
        for j in a[1:]:
            if j == this or j < this - 3:
                return False
            this = j
    else:
        return False
    return True

def checkrem(a):
    safe = False
    for i in range(len(a)):
        if checkone(a[:i]+a[i+1:]):
            safe = True
            break
    return safe

for i in data:
    a = [int(n) for n in i.split(" ")]
    if checkone(a):
        total += 1
    elif checkrem(a):
        total2 += 1
    
print("safe:",total,"\nsafe with removal:",total2,"\ntotal:",total+total2)
