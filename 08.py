import sys
lines = []
#import regex
import re
from functools import cmp_to_key
from math import gcd

with open('inputs/08.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

dirs = lines[0]
rest = lines[2:]
dirmap = {}

for line in rest:
    node = line.split(" = ")[0]
    left = line.split(" = ")[1].split("(")[1].split(",")[0]
    right = line.split(" = ")[1].split(")")[0].split(", ")[1]
    print(node, left, right)
    dirmap[node] = (left, right)

found = False
currs =[]
for key in dirmap:
    if key.endswith("A"):
        currs.append(key)
print(currs)
count = 0


periodmap = {}

def lcm(list):
    lcm = 1
    for i in list:
        lcm = lcm*i//gcd(lcm, i)
    return lcm


while not found:
    # print("loop")
    for char in dirs:
        for (i, curr) in enumerate(currs):
            # print(i, curr)
            if char == "L":
                currs[i] = dirmap[curr][0]
            elif char == "R":
                currs[i] = dirmap[curr][1]
        count += 1
        # print(count)
        
        #check if all end in Z
        # print(currs)
        for (i, curr) in enumerate(currs):
            if curr.endswith("Z"):
                if i not in periodmap:
                    periodmap[i] = count
                    print('added to periodmap', curr, count)
                
                # print(i, count, curr)
        if all([curr.endswith("Z") for curr in currs]):
            found = True
            break
        if len(periodmap) == 6:
            found = True
            break



print(count)
print(periodmap)
print(lcm([x for x in periodmap.values()]))