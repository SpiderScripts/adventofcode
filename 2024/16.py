data = open("16input.txt","r").read()

'''
data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
'''
g = [[]]
r = 0

# set up grid system
for i in data:
    if i == "E":
        e = [(r,len(g[r]),0,1),(r,len(g[r]),0,-1),(r,len(g[r]),1,0),(r,len(g[r]),-1,0)]
    if i == "S":
        s = (r,len(g[r]),0,1)
    if i == "\n":
        r += 1
        g.append([])
    else:
        g[r] += [i]

# find adjacent empty cells, and what direction we approach them from
def adj(c):
    turn = [(0,1),(1,0),(0,-1),(-1,0)]
    a = []
    x = c[0]
    y = c[1]
    d = (c[2],c[3])
    if g[x+1][y] != "#":
        t = (turn.index(d) - turn.index((1,0)))%4
        a.append([(x+1,y,1,0),t,"v"])
    if g[x-1][y] != "#":
        t = (turn.index(d) - turn.index((-1,0)))%4
        a.append([(x-1,y,-1,0),t,"^"])
    if g[x][y+1] != "#":
        t = (turn.index(d) - turn.index((0,1)))%4
        a.append([(x,y+1,0,1),t,">"])
    if g[x][y-1] != "#":
        t = (turn.index(d) - turn.index((0,-1)))%4
        a.append([(x,y-1,0,-1),t,"<"])
    return a

q = {s:[0,[],"."]}
v = {}

while q:
    m = min(q, key=q.get)
    t = q.pop(m)
    x = t[0]
    v[m] = [x,t[1],t[2]]
    d = (m[2],m[3])
    n = adj(m)
    for i in n:
        if i[0] not in v:
            if i[1] == 3: i[1] = 1
            step = x + 1 + i[1]*1000
            if i[0] in q:
                if step < q[i[0]][0]:
                    q[i[0]] = [step,[m],i[2]]
                elif step == q[i[0]][0]:
                    q[i[0]][1] += [m]
            else:
                q[i[0]] = [step,[m],i[2]]

# check all ways of reaching goal
end = []
for i in e:
    if i in v:
        end.append(v[i])

# backtracking
q = []
q += min(end)[1]
c = 1
back = [(e[0][0],e[0][1])]

while q:
    t = q.pop()
    # ignore turning, only count steps
    if (t[0],t[1]) not in back:
        c += 1
        back.append((t[0],t[1]))
    q += v[t][1]

print(min(end)[0])
print(c)

