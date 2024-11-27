f = open("03input.txt",'r')

data = f.readline()

x = 0
y = 0

visited = []

for i in data[0::2]:
    if i == ">":
        x += 1
    elif i == "<":
        x -= 1
    elif i == "^":
        y += 1
    elif i == "v":
        y -= 1
    cur = [x,y]
    if cur in visited:
        pass
    else:
        visited.append(cur)

x = 0
y = 0

for i in data[1::2]:
    if i == ">":
        x += 1
    elif i == "<":
        x -= 1
    elif i == "^":
        y += 1
    elif i == "v":
        y -= 1
    cur = [x,y]
    if cur in visited:
        pass
    else:
        visited.append(cur)

print(len(visited))
