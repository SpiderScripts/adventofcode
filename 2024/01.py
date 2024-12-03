f = open("01input.txt","r")
data = f.readlines()

'''
data = ["3   4",
"4   3",
"2   5",
"1   3",
"3   9",
"3   3"]
'''

total = 0
left = []
right = []

for i in data:
    a = i.split("   ")
    left.append(int(a[0]))
    right.append(int(a[1]))

left.sort()
right.sort()

for i in range(len(left)):
    total += abs(left[i]-right[i])

print(total)

total2 = 0

for i in range(len(left)):
    total2+= left[i]*right.count(left[i])

print(total2)
