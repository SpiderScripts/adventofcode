f = open("08input.txt",'r')

data = f.readlines()

forest = []

for i in data:
    forest.append(i.strip())

'''
visible = set([])

# rows
for i in range(len(forest)):
    lmax = -1
    rmax = -1
    for j in range(len(forest[i])):
        l = forest[i][j]
        r = forest[i][len(forest[i]) - j - 1]
        if int(l) > lmax:
            lmax = int(l)
            visible.add(str(i)+":"+str(j))
        if int(r) > rmax:
            rmax = int(r)
            visible.add(str(i)+":"+str(len(forest[i]) - j - 1))

for j in range(len(forest[0])):
    umax = -1
    dmax = -1
    for i in range(len(forest)):
        d = forest[i][j]
        u = forest[len(forest) - i - 1][j]
        if int(d) > umax:
            umax = int(d)
            visible.add(str(i)+":"+str(j))
        if int(u) > dmax:
            dmax = int(u)
            visible.add(str(len(forest) - i - 1)+":"+str(j))

print(len(visible))
'''

def scenic_score(x,y,h):
    l = 0
    xl = x
    while True:
        if xl == 0:
            break
        xl -= 1
        l += 1
        if forest[xl][y] >= h:
            break
    r = 0
    xr = x
    while True:
        if xr == 98:
            break
        xr += 1
        r += 1
        if forest[xr][y] >= h:
            break
    u = 0
    yu = y
    while True:
        if yu == 0:
            break
        yu -= 1
        u += 1
        if forest[x][yu] >= h:
            break
    d = 0
    yd = y
    while True:
        if yd == 98:
            break
        yd += 1
        d += 1
        if forest[x][yd] >= h:
            break
    return l*r*u*d

best_view = 0

for i in range(99):
    for j in range(99):
        view = scenic_score(i,j,forest[i][j])
        best_view = max(best_view,view)

print(best_view)
