data = open("04input.txt","r").read().splitlines()

'''
data = [".M.S......",
"..A..MSMS.",
".M.S.MAA..",
"..A.ASMSM.",
".M.S.M....",
"..........",
"S.S.S.S.S.",
".A.A.A.A..",
"M.M.M.M.M.",
".........."]
'''

t1,t2 = 0,0

w,h = len(data[0]), len(data)
p1,p2 = ("XMAS","SAMX"), ("MAS","SAM")

for i in range(h):
    for j in range(w):
        if j < w - 3:
            a = data[i][j:j+4]
            if a in p1: t1 += 1
        if i < h - 3:
            a = "".join([data[i+a][j] for a in range(4)])
            if a in p1: t1 += 1
        if j < w - 3 and i < h - 3:
            a = "".join([data[i+a][j+a] for a in range(4)])
            if a in p1: t1 += 1
            a = "".join([data[i+3-a][j+a] for a in range(4)])
            if a in p1: t1 += 1
        if j < w - 2 and i < h - 2:
            a = "".join([data[i+a][j+a] for a in range(3)])
            b = "".join([data[i+2-a][j+a] for a in range(3)])
            if (a in p2) and (b in p2): t2 += 1

print(t1)
print(t2)
