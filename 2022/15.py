def main():
    f = open("15input.txt",'r')
    data = f.readlines()
    '''
    data = ["Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n",
    "Sensor at x=9, y=16: closest beacon is at x=10, y=16\n",
    "Sensor at x=13, y=2: closest beacon is at x=15, y=3\n",
    "Sensor at x=12, y=14: closest beacon is at x=10, y=16\n",
    "Sensor at x=10, y=20: closest beacon is at x=10, y=16\n",
    "Sensor at x=14, y=17: closest beacon is at x=10, y=16\n",
    "Sensor at x=8, y=7: closest beacon is at x=2, y=10\n",
    "Sensor at x=2, y=0: closest beacon is at x=2, y=10\n",
    "Sensor at x=0, y=11: closest beacon is at x=2, y=10\n",
    "Sensor at x=20, y=14: closest beacon is at x=25, y=17\n",
    "Sensor at x=17, y=20: closest beacon is at x=21, y=22\n",
    "Sensor at x=16, y=7: closest beacon is at x=15, y=3\n",
    "Sensor at x=14, y=3: closest beacon is at x=15, y=3\n",
    "Sensor at x=20, y=1: closest beacon is at x=15, y=3"]
    '''
    
    sensors = parse(data)
    # part 1
    num = checkrow(2000000,sensors)
    print(num)

    # part 2
    for y in range(3000000,4000000):
        num = checkrow(y,sensors)
        if len(num) > 1:
            print("\n",y,num)
        if y % 100000 == 0:
            print(".",end="")
    
def checkrow(y,s):
    ranges = []
    for j in s:
        ydist = abs(j[1]-y)
        xdist = max(j[4] - ydist,0)
        if xdist > 0:
            ranges.append((j[0]-xdist,j[0]+xdist))
    b = []
    for begin,end in sorted(ranges):
        if b and b[-1][1] >= begin - 1:
            b[-1][1] = max(b[-1][1], end)
        else:
            b.append([begin, end])
    return b
    
def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def parse(data):
    sensors = []
    for i in data:
        bits = i.split(",")
        sensorx = int(bits[0][12:])
        sensory = int(bits[1].split(":")[0][3:])
        beaconx = int(bits[1].split(":")[1][24:])
        beacony = int(bits[2][3:].strip())
        dist = abs(sensorx - beaconx) + abs(sensory - beacony)
        sensors.append([sensorx,sensory,beaconx,beacony,dist])
    return sensors

if __name__ == "__main__":
    main()
