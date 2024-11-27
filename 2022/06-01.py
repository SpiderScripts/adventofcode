f = open("06input.txt",'r')

data = f.readline()

print(data)

a = 'g'
b = 'g'
c = 'g'
d = 'g'

pos = 1

for i in data:
    a,b,c,d = b,c,d,i
    if len(set([a,b,c,d])) == 4:
        print(pos)
        break
    pos += 1
