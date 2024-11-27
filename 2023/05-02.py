import re

f = open("05input.txt",'r')

data = f.readlines()

'''
data = ["seeds: 79 14 55 13",
"",
"seed-to-soil map:",
"50 98 2",
"52 50 48",
"",
"soil-to-fertilizer map:",
"0 15 37",
"37 52 2",
"39 0 15",
"",
"fertilizer-to-water map:",
"49 53 8",
"0 11 42",
"42 0 7",
"57 7 4",
"",
"water-to-light map:",
"88 18 7",
"18 25 70",
"",
"light-to-temperature map:",
"45 77 23",
"81 45 19",
"68 64 13",
"",
"temperature-to-humidity map:",
"0 69 1",
"1 0 69",
"",
"humidity-to-location map:",
"60 56 37",
"56 93 4"]
'''

def findseeds(data):
    lowest = 9999999999
    values = [int(x) for x in data.split(":")[1].strip().split(" ")]
    pairs = len(values)//2
    for i in range(pairs):
        start = values[2*i]
        length = values[2*i+1]
        print(i,length)
        for j in range(length):
            if j % 100000 == 0:
                print(".",end="")
            track = trace(start+j)
            if track[7] < lowest:
                lowest = track[7]
    return lowest

def parse(data):
    maps = []
    this = []
    mapno = 1
    for i in data:
        if i.strip() == "":
            maps.append(this)
            this = []
        elif ":" in i:
            pass
        else:
            this.append([int(x) for x in i.split(" ")])
    maps.append(this)
    return maps

def trace(seed):
    track = [seed]
    this = seed
    for i in maps:
        match = False
        for j in i:
            gap = this - j[1]
            if gap <= j[2] and gap >= 0:
                this = j[0] + gap
                match = True
                break
        track.append(this)
    return track

maps = parse(data[2:])

lowest = findseeds(data[0])

print(lowest)
