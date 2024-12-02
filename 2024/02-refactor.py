f = open("02input.txt",'r')

data = f.readlines()

'''
data = ["7 6 4 2 1",
"1 2 7 8 9",
"9 7 6 2 1",
"1 3 2 4 5",
"8 6 4 4 1",
"1 3 6 7 9"]
'''

total = 0
total2 = 0

def check(a):
    diff = [a[i+1]-a[i] for i in range(len(a)-1)]
    if all(d > 0 and d <= 3 for d in diff) or all(d < 0 and d >= -3 for d in diff):
        return True
    return False

def checkrem(a):
    for i in range(len(a)):
        if check(a[:i]+a[i+1:]):
            return True
    return False

for i in data:
    a = [int(n) for n in i.split(" ")]
    if check(a):
        total += 1
    elif checkrem(a):
        total2 += 1
    
print("safe:",total,"\nsafe with removal:",total2,"\ntotal:",total+total2)
