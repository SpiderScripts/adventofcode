import itertools
import time
start = time.time()

data = open("10input.txt","r").read()

'''data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
'''
data = data.splitlines()
total1 = 0
total2 = 0
w = len(data[0])
h = len(data)
s = []
e = {}

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "0": s.append([i,j])

def path(s):
    q = [s]
    d = [0]
    while q:
        this = q.pop(0)
        x = this[0]
        y = this[1]
        val = int(data[x][y])
        if val == 9:
            d[0] += 1
            if this not in d:
                d.append(this)
        else:
            n = str(val+1)
            if x < h-1:
                if data[x+1][y] == n: q.append([x+1,y])
            if x > 0:
                if data[x-1][y] == n:
                    q.append([x-1,y])
            if y < w-1:
                if data[x][y+1] == n:
                    q.append([x,y+1])
            if y > 0:
                if data[x][y-1] == n:
                    q.append([x,y-1])
    return d

for i in s:
    this = path(i)
    total1 += len(this[1:])
    total2 += this[0]

print(total1)
print(total2)
print(time.time() - start)
