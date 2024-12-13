import numpy
from math import gcd

data = open("13input.txt","r").read()

'''
data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
'''

data = data.splitlines()
t = 0

def xy(a):
    a = a.split(",")
    x = int(a[0])
    y = int(a[1][3:])
    return [x,y]

def solve(a,b,x):
    a = xy(a)
    b = xy(b)
    x = xy(x)
    x[0] += 10000000000000
    x[1] += 10000000000000
    s = numpy.linalg.solve([[a[0],b[0]],[a[1],b[1]]],x)
    return [s[0],s[1]]

for i in range(len(data)//4+1):
    s = solve(data[i*4][11:],data[i*4+1][11:],data[i*4+2][9:])
    # there must be a better way of checking it's an integer!
    if (int(round(s[0],2)) == round(s[0],2)) and (int(round(s[1],2)) == round(s[1],2)):
        t += 3*round(s[0]) + round(s[1])

print(t)
