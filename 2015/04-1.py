import re

f = open("04input.txt",'r')

data = f.readlines()

nice = 0

for i in data:
    if len(re.findall("[aeiou]", i)) >= 3:
        if (re.search("(.)\\1{1,}",i)):
            if not (re.search("ab|cd|pq|xy",i)):
                nice += 1

print(nice)

nice = 0

for i in data:
    if (re.search("(..).*\\1{1,}",i)):
        if (re.search("(.).\\1{1,}",i)):
            print(i)
            nice += 1

print(nice)
