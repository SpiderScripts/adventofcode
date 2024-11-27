f = open("12input.txt",'r')

data = f.readlines()

rows = len(data)
cols = len(data[0].strip())

graph = {}

# build connected graph
for x in range(rows):
    for y in range(cols):
        this = data[x][y]
        if this == "S":
            this = "a"
        adj = []
        if x > 0 and ord(this) + 1 >= ord(data[x-1][y]):
                adj.append((x-1)*cols+y)
        if x < 40 and ord(this) + 1 >= ord(data[x+1][y]):
                adj.append((x+1)*cols+y)
        if y > 0 and ord(this) + 1 >= ord(data[x][y-1]):
                adj.append(x*cols+(y-1))
        if y < 153 and ord(this) + 1 >= ord(data[x][y+1]):
                adj.append(x*cols+(y+1))
        graph[x*cols+y] = adj

# search for shortest path
def bfs(visited, g, node):
    visited.append([node,"start"])
    breadcrumb[node] = "start"
    queue.append(node)

    while queue:
        s = queue.pop(0)
        #print(s)

        for neighbour in g[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                breadcrumb[neighbour] = s
                queue.append(neighbour)
            if neighbour == 3212:
                return True
        else:
            continue  # only executed if the inner loop did NOT break
        break

# check length of path using breadcrumb trail
def retrace(trail,goal,start):
#    print(start)
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = breadcrumb[cur]
    return len(path)

shortest = 472

for i in range(6314):
    if data[i//cols][i%cols] == "a":
        visited = [] # List to keep track of visited nodes.
        breadcrumb = {}
        queue = []     #Initialize a queue
        if (bfs(visited,graph,i)):
            length = retrace(breadcrumb,3212,i)
            shortest = min(shortest,length)#
            print(i,length,shortest)

print(shortest)
