import itertools

data = open("08input.txt","r").read().splitlines()

'''
data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

data = data.splitlines()
'''

ant = {}
hotspot = set()

h = len(data)
w = len(data[0])


for i in range(h):
    for j in range(w):
        this = data[i][j]
        if this != ".":
            if this in ant:
                ant[this] += [(i,j)]
            else:
                ant[this] = [(i,j)]

for i in ant:
    for j in itertools.combinations(ant[i],2):
        gx = j[0][0]-j[1][0]
        gy = j[0][1]-j[1][1]
        x,y=j[0]
        while True:
            hotspot.add((x,y))
            x += gx
            y += gy
            if not(0<=x<h and 0<=y<w):
                break
        x,y=j[1]
        while True:
            hotspot.add((x,y))
            x -= gx
            y -= gy
            if not(0<=x<h and 0<=y<w):
                break

print(len(hotspot))
