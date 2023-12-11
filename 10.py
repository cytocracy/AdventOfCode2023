import sys
lines = []
#import regex
import re
from functools import cmp_to_key
from math import gcd

with open('inputs/10.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))


neighbors = {}
tiles = {}
start = (0, 0)
usedpipes = set()
ground = set()


for (i, line) in enumerate(lines):
    for (j, char) in enumerate(line):
        tiles[(i, j)] = char
        if char == ".":
            ground.add((i, j))
            continue
        if char == "|":
            neighbors[(i, j)] = [(i-1, j), (i+1, j)]
        if char == "-":
            neighbors[(i, j)] = [(i, j-1), (i, j+1)]
        if char == "L":
            neighbors[(i,j)] = [(i-1, j), (i, j+1)]
        if char == "J":
            neighbors[(i,j)] = [(i-1, j), (i, j-1)]
        if char == "7":
            neighbors[(i,j)] = [(i+1, j), (i, j-1)]
        if char == "F":
            neighbors[(i,j)] = [(i+1, j), (i, j+1)]
        if char == "S":
            start = (i, j)

neighbors[start] = [(x[0], x[1]) for x in neighbors if start in neighbors[x]]
# print(neighbors[start])
# print(start)
def get_neighbors(node):
    print(node)
    return neighbors[node]

def bfs(n1, n2):
    queue = [n1]
    visited = [n1]
    parent = {n1: None}

    while queue:
        current = queue.pop(0)
        if current == n2:
            temp = current
            path = []
            while temp != None:
                usedpipes.add(temp)
                path.append(temp)
                temp = parent[temp]
            if len(path) > 2:
                return path[::-1]
            else:
                visited.remove(n2)
                parent[n2] = None
        # print(current)
        # print(neighbors[current])
        for neighbor in neighbors[current]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                parent[neighbor] = current




fakestart = neighbors[start][0]
fakeend = neighbors[start][1]
neighbors[start] = []
usedpipes.add(start)


print((len(bfs(fakestart, fakeend))+1)/2)


neighbors[start] = [x for x in usedpipes if start in neighbors[x]]
ground = set(x for x in tiles if x not in usedpipes)

print(neighbors[start])
diffs = [(x[0] - start[0], x[1] - start[1]) for x in neighbors[start]]
print(diffs)
if (0, 1) in diffs and (1, 0) in diffs:
    tiles[start] = "F"
elif (0, 1) in diffs and (-1, 0) in diffs:
    tiles[start] = "L"
elif (0, -1) in diffs and (-1, 0) in diffs:
    tiles[start] = "J"
elif (0, -1) in diffs and (1, 0) in diffs:
    tiles[start] = "7"
elif (0, 1) in diffs and (0, -1) in diffs:
    tiles[start] = "-"
elif (1, 0) in diffs and (-1, 0) in diffs:
    tiles[start] = "|"
else:
    print("error")
    print(diffs)
    print(neighbors[start])
    sys.exit(1)
    
print(tiles[start])



# print(neighbors[start])




def countpipes(loc):
    dir = (0,1)
    curr = loc
    count = 0
    while (curr[0], curr[1] + 1) in tiles:
        curr = (curr[0], curr[1]+1)
        # print(curr)
        if curr in usedpipes:
            if curr == start:
                print("start")
            # print("used")
            if tiles[curr] == "L":
                temp = (curr[0], curr[1] + 1)
                while tiles[temp] == "-":
                    temp = (temp[0], temp[1] + 1)
                curr = temp
                if tiles[temp] == "J":
                    count += 2
                    # print("LJ")
                else:
                    count += 1
                    # print("L7")
            elif tiles[curr] == "F":
                # print('found f')
                temp = (curr[0], curr[1] + 1)
                while tiles[temp] == "-":
                    temp = (temp[0], temp[1] + 1)
                    # print('itr')
                curr = temp
                if tiles[temp] == "7":
                    count += 2
                    # print("F7")
                else:
                    count += 1
                    # print("FJ")
            else:
                count += 1
                # print(tiles[curr])
    return count


            
def getinside(loc):
    return not (countpipes(loc) % 2 == 0)


# print(getinside((0, 3)))
inside = set()
sum = 0
for tile in ground:
    if getinside(tile):
        inside.add(tile)
        sum += 1

printstrings = lines
# print(usedpipes)
for i in range(len(printstrings)):
    for j in range(len(printstrings[i])):
        if (i, j) == start:
            printstrings[i] = printstrings[i][:j] + "." + printstrings[i][j+1:]
        elif (i, j) not in usedpipes:
            printstrings[i] = printstrings[i][:j] + " " + printstrings[i][j+1:]
        else:
            printstrings[i] = printstrings[i][:j] + "." + printstrings[i][j+1:]
            pass
        if (i, j) in inside:
            printstrings[i] = printstrings[i][:j] + "I" + printstrings[i][j+1:]
        elif (i, j) in ground:
            printstrings[i] = printstrings[i][:j] + " " + printstrings[i][j+1:]

for line in printstrings:
    print(line)


# print(countpipes((4, 7)))

print(sum)
# print(start in usedpipes)







# print(neighbors)