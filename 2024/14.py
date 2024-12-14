data = open("14input.txt","r").read()

'''
data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
'''
data = data.splitlines()

p = []
v = []
w = 101
h = 103

for i in data:
    a = i.split()
    p.append([int(x) for x in a[0][2:].split(",")])
    v.append([int(x) for x in a[1][2:].split(",")])

def step():
    for i in range(len(p)):
        p[i][0] = (p[i][0] + v[i][0]) % w
        p[i][1] = (p[i][1] + v[i][1]) % h


def count():
    q = [0,0,0,0]
    for i in p:
        if i[0] < w//2 and i[1] < h//2:
            q[0] += 1
        elif i[0] > w//2 and i[1] < h//2:
            q[1] += 1
        elif i[0] < w//2 and i[1] > h//2:
            q[2] += 1
        elif i[0] > w//2 and i[1] > h//2:
            q[3] += 1
    return q[0]*q[1]*q[2]*q[3]

# tree?  nah let's brute force search for a straight line and hope for the best...
def line():
    for i in range(h):
        c = 0
        for j in range(w):
            if [j,i] in p:
                c += 1
            else:
                c = 0
            if c == 10:
                return True

c = 0

while True:
    step()
    c += 1
    if line():
        break
    if c % 10 == 0:
        # it's so slow, lets print the counter to check it hasn't broken!
        print(c)

print(c,p)
