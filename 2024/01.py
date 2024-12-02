f = open("01input.txt","r")

data = f.readlines()

data = ["3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3"]

l = sorted([int(a.split("   ")[0]) for a in data])
r = sorted([int(a.split("   ")[1]) for a in data])

t1 = sum(abs(l[i] - r[i]) for i in range(len(l)))
t2 = sum(i*r.count(i) for i in l)

print(t1,t2,sep="\n")