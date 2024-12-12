import time
start = time.time()

data = open("12input.txt","r").read()
'''
data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

data = """AAAB
ABAB
BAAB
BBBB"""
'''
data = data.splitlines()

t1 = 0
t2 = 0
visited = []
h = len(data)
w = len(data[0])

def check(s,l):
    n = []
    e = []
    v = 0
    q = [s]
    while q:
        this = q.pop(0)
        n.append(this)
        x = this[0]
        y = this[1]
        if x < h-1:
            if [x+1,y] not in n and [x+1,y] not in q:
                if data[x+1][y] == l:
                    q.append([x+1,y])
                else:
                    e.append([x+1,y])
        else: e.append([x+1,y])
        if x > 0:
            if [x-1,y] not in n and [x-1,y] not in q:
                if data[x-1][y] == l:
                    q.append([x-1,y])
                else:
                    e.append([x,y])
        else: e.append([x,y])
        if y < w-1:
            if [x,y+1] not in n and [x,y+1] not in q:
                if data[x][y+1] == l:
                    q.append([x,y+1])
                else:
                    e.append([x,y+1])
        else: e.append([x,y+1])
        if y > 0:
            if [x,y-1] not in n and [x,y-1] not in q:
                if data[x][y-1] == l:
                    q.append([x,y-1])
                else:
                    e.append([x,y])
        else: e.append([x,y])

    for i in n:
        x = i[0]
        y = i[1]
        t = [x-1,y] in n
        b = [x+1,y] in n
        l = [x,y-1] in n
        r = [x,y+1] in n
        tl = [x-1,y-1] in n
        tr = [x-1,y+1] in n
        bl = [x+1,y-1] in n
        br = [x+1,y+1] in n
        if not t and not l:
            v += 1
        if not l and not b:
            v += 1
        if not b and not r:
            v += 1
        if not r and not t:
            v += 1
        if t and l and not tl:
            v += 1
        if l and b and not bl:
            v += 1
        if b and r and not br:
            v += 1
        if r and t and not tr:
            v += 1

    return (n,e,v)

for i in range(h):
    for j in range(w):
        if [i,j] not in visited:
            r = check([i,j],data[i][j])
            visited += r[0]
            t1 += len(r[0])*len(r[1])
            t2 += len(r[0])*r[2]

print(t1)
print(t2)
print(time.time() - start)
