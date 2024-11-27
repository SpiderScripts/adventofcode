import re

f = open("06input.txt",'r')

data = f.readlines()


data = ["Time:      7  15   30",
"Distance:  9  40  200"]

'''
data = ["Time:        51     69     98     78",
"Distance:   377   1171   1224   1505"]
'''

races = [[51699878,377117112241505]]

total = 1

for i in races:
    win = 0
    for j in range(i[0]):
        distance = j*(i[0]-j)
        if distance > i[1]:
            win += 1
    total *= win

print(total)
