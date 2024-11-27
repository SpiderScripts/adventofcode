import re

f = open("01input.txt",'r')

data = f.readlines()

'''
data = ["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]
'''

total = 0

def first_last(string):
    firstpos = len(string)
    first = 0
    lastpos = -1
    last = 0
    hunt = ["zero","one","two","three","four","five","six","seven","eight","nine","0","1","2","3","4","5","6","7","8","9"]
    for i in range(len(hunt)):
        try:
            if string.index(hunt[i]) < firstpos:
                firstpos = string.index(hunt[i])
                first = i%10
            if string.rindex(hunt[i]) > lastpos:
                lastpos = string.rindex(hunt[i])
                last = i%10
        except:
            pass
    return (10*first + last)

for i in data:
    total += first_last(i)
    
print(total)
