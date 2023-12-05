import sys
lines = []

with open('inputs/05.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

seeds = lines[0].split(": ")[1].split(" ")



print(seeds)
print(lines)
seedtosoilindex = lines.index("seed-to-soil map:") + 1
seedtosoilmap = []

def mapthing(inp, triples):
    for (dest, src, rge) in triples:
        if inp >= src and inp < src + rge:
            return dest + inp - src
    return inp


for i in range(seedtosoilindex, len(lines)):
    print(i)
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        seedtosoilmap.append((dest, src, rge))

        

soiltofertilizerindex = lines.index("soil-to-fertilizer map:") + 1
soiltofertilizermap = []

for i in range(soiltofertilizerindex, len(lines)):
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        soiltofertilizermap.append((dest, src, rge))


ferttowaterindex = lines.index("fertilizer-to-water map:") + 1
ferttowatermap = []

for i in range(ferttowaterindex, len(lines)):
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        ferttowatermap.append((dest, src, rge))

watertolightindex = lines.index("water-to-light map:") + 1
watertolightmap = []
for i in range(watertolightindex, len(lines)):
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        watertolightmap.append((dest, src, rge))

lighttotempindex = lines.index("light-to-temperature map:") + 1
lighttotempmap = []

for i in range(lighttotempindex, len(lines)):
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        lighttotempmap.append((dest, src, rge))


temptohumidityindex = lines.index("temperature-to-humidity map:") + 1
temptohumiditymap = []

for i in range(temptohumidityindex, len(lines)):
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        temptohumiditymap.append((dest, src, rge))

humiditytolocationindex = lines.index("humidity-to-location map:") + 1
humiditytolocationmap = []

for i in range(humiditytolocationindex, len(lines)):
    if lines[i] == "":
        break
    else:
        dest, src, rge = lines[i].split(" ")
        dest = int(dest)
        src = int(src)
        rge = int(rge)

        humiditytolocationmap.append((dest, src, rge))

def getseedtolocation(seed):
    soil = mapthing(seed, seedtosoilmap)
    fertilizer = mapthing(soil, soiltofertilizermap)
    water = mapthing(fertilizer, ferttowatermap)
    light = mapthing(water, watertolightmap)
    temp = mapthing(light, lighttotempmap)
    humidity = mapthing(temp, temptohumiditymap)
    location = mapthing(humidity, humiditytolocationmap)

    return location

min = 9999999999999
seednums = []
seedranges = []
for (i, seed) in enumerate(seeds):
    if i % 2 == 0:
        seednums.append(int(seed))
    else:
        seedranges.append(int(seed))


#find min value of values of humitidy to location



dp = []
for (i, seed) in enumerate(seednums):
    for j in range(seednums[i], seednums[i] + seedranges[i]):
        if j < len(dp) and dp[j] != None:
            continue
        if getseedtolocation(j) < min:
            min = getseedtolocation(j)
        dp.insert(j, getseedtolocation(j))
    # if getseedtolocation(int(seed)) < min:
    #     min = getseedtolocation(int(seed))

print(min)
