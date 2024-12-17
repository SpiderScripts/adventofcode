data = open("17input.txt","r").readlines()
a = int(data[0][12:])
goal = data[4].strip()[9:]
i = eval("["+goal+"]")

co = ["0","1","2","3","a","b","c"]

def test(a):
    b = 0
    c = 0
    p = 0
    out = ""

    while p < len(i):
        x = i[p]
        y = i[p+1]
        p += 2
        if x == 0:
            a = a // 2**eval(co[y])
        elif x == 1:
            b = b ^ y
        elif x == 2:
            b = eval(co[y])%8
        elif x == 3:
            if a != 0: p = y
        elif x == 4:
            b = b ^ c
        elif x == 5:
            out += str((eval(co[y])%8)) + ","
        elif x == 6:
            b = a // 2**eval(co[y])
        elif x == 7:
            c = a // 2**eval(co[y])

    out = out[:-1]
    return out

# part 1:
print(test(a))

# part 2:
q = [[]]
sol = []

while q:
    s = q.pop(0)
    for j in range(8):
        a = 0
        for k in s:
            a = (a<<3) + k
        this = test((a<<3)+j)
        if this == goal:
            sol.append((a<<3)+j)
        if this == goal[-len(this):]:
            q.append(s+[j])

print(min(sol))
