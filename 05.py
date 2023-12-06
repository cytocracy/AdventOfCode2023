import sys
lines = []

with open('inputs/05.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

seeds = lines[0].split(": ")[1].split(" ")

PART = 2

# print(seeds)
# print(lines)
seedtosoilindex = lines.index("seed-to-soil map:") + 1
seedtosoilmap = []

def mapthing(inp, triples):
    for (dest, src, rge) in triples:
        if inp >= src and inp < src + rge:
            return dest + inp - src
    return inp


for i in range(seedtosoilindex, len(lines)):
    # print(i)
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

champmin = 999999999999
seednums = []
seedranges = []
for (i, seed) in enumerate(seeds):
    if i % 2 == 0:
        seednums.append(int(seed))
    else:
        seedranges.append(int(seed))


#find min value of values of humitidy to location

def getrange(triple):
    dest, src, rge = triple
    return (src, src + rge-1, dest-src)

def fillrange(sortedranges, maxend):
    sortedranges = sorted(sortedranges, key=lambda x: x[0])
    for i in range(len(sortedranges)-1):
        if sortedranges[i][1] + 1 < sortedranges[i+1][0]:
            sortedranges.insert(i+1, (sortedranges[i][1] + 1, sortedranges[i+1][0] - 1, 0))
    if sortedranges[0][0] != 0:
        sortedranges.insert(0, (0, sortedranges[0][0] - 1, 0))
    if sortedranges[-1][1] != maxend:
        sortedranges.append((sortedranges[-1][1] + 1, maxend, 0))
    return sortedranges




def overlap(range1, range2):
    start1, end1, val1 = range1
    start2, end2, val2 = range2
    if end1 < start2:
        return False
    if start1 > end2:
        return False
    return True

def convert(triple):
    low, high, add = triple
    return (low+add, high+add)

def mutate(seeds, newranges):
    # print('newranges: ', newranges)
    i = 0
    untested = seeds.copy()
    newseeds = []
    while len(untested) > 0:
        # seed = seeds.pop(0)
        seed = untested.pop(0)
        # j = 0
        replaceranges = []
        # untested = [seeds[i]]
        j=0
        # untested = [seeds[i]]
        while j < len(newranges):
            
            if overlap((seed[0], seed[1], 0), newranges[j]):
                print('overlap: ', seed, newranges[j])
                if newranges[j][0] <= seed[0] and newranges[j][1] >= seed[1]: #all overlap
                    newseeds.append(convert((seed[0], seed[1], newranges[j][2])))
                    
                    # print('append1')
                elif newranges[j][0] > seed[0] and newranges[j][1] >= seed[1]: # right overlap
                    newseeds.append(convert((newranges[j][0], seed[1], newranges[j][2])))
                    untested.append((seed[0], newranges[j][0]-1, 0))
                    
                    # seed = (seed[0], newranges[j][0]-1)
                    # replaceranges.append((seed[0], newranges[j][0]-1, 0))
                    # print('append2')
                
                elif newranges[j][0] <= seed[0] and newranges[j][1] < seed[1]: #left overlap
                    newseeds.append(convert((seed[0], newranges[j][1], newranges[j][2])))
                    
                    ##ONLY IF OTHERS DON'T OVERLAP TOO
                    #HOW TO FIX?
                    

                    untested.append((newranges[j][1]+1, seed[1], 0))
                    
                    # seed = (newranges[j][1]+1, seed[1])
                    # replaceranges.append((newranges[j][1]+1, seed[1], 0))
                    # print('append3')
                
                else: # middle overlap
                    newseeds.append(convert((newranges[j][0], newranges[j][1], newranges[j][2])))
                    untested.append((seed[0], newranges[j][1]-1, 0))
                    untested.append((newranges[j][0]+1, seed[1], 0))
                    # seed = (seed[0], newranges[j][1]-1)
                    # seeds.append((newranges[j][0]+1, seed[1]))
                    # print('append4')
                # print('append5')
                break
            
            j += 1
        
        
        # seeds.pop(i)
        # if len(replaceranges) == 0:
        #     replaceranges.append((seed[0], seed[1], 0))
        # replaceranges = [(x+add, y+add) for (x, y, add) in replaceranges]
        # # print('replaceranges: ', replaceranges)
        # # print('adding in: ', replaceranges)
        # seeds = seeds + replaceranges
        # numskip = len(replaceranges)
        # seeds = sorted(seeds, key=lambda x: x[0])
        # i += numskip
        # # print('i: ', i)
    return newseeds


if PART == 1:
    pass
elif PART == 2:
    seedmapranges = [getrange(triple) for triple in seedtosoilmap]
    soilranges = [getrange(triple) for triple in soiltofertilizermap]
    fertilizerranges = [getrange(triple) for triple in ferttowatermap]
    waterranges = [getrange(triple) for triple in watertolightmap]
    lightranges = [getrange(triple) for triple in lighttotempmap]
    tempranges = [getrange(triple) for triple in temptohumiditymap]
    humidityranges = [getrange(triple) for triple in humiditytolocationmap]
    
   

    # allranges= [seedmapranges, soilranges, fertilizerranges, waterranges, lightranges, tempranges, humidityranges]
    # allranges = [sorted(ranges, key=lambda x: x[0]) for ranges in allranges]
    # print('allranges\n', allranges)
    maxend = 999999999999
    
    # allranges = [fillrange(ranges, maxend) for ranges in allranges]




    initseeds = []
    for i in range(len(seednums)):
        initseeds.append((seednums[i], seednums[i] + seedranges[i]-1))
    initseeds = sorted(initseeds, key=lambda x: x[0])

    print('seedmapranges\n', fillrange(seedmapranges, maxend))
    print(initseeds)


    initseeds = mutate(initseeds, fillrange(seedmapranges, maxend))
    print("1")
    initseeds = mutate(initseeds, fillrange(soilranges, maxend))
    print(initseeds)
    print("2")
    initseeds = mutate(initseeds, fillrange(fertilizerranges, maxend))
    print(initseeds)
    print("3")
    initseeds = mutate(initseeds, fillrange(waterranges, maxend))
    print(initseeds)
    print("4")
    initseeds = mutate(initseeds, fillrange(lightranges, maxend))
    print(initseeds)
    print("5")
    initseeds = mutate(initseeds, fillrange(tempranges, maxend))
    print(initseeds)
    print("6")
    initseeds = mutate(initseeds, fillrange(humidityranges, maxend))
    print(initseeds)

  
    initseeds = sorted(initseeds, key=lambda x: x[0])
    minloc = initseeds[0][0]
    
    print('minloc: ', minloc)

