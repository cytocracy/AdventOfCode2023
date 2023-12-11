import sys
lines = []
#import regex
import re
from functools import cmp_to_key
from math import gcd

with open('inputs/11.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

lines = [[x for x in line] for line in lines]
clean = lines.copy()
multrows = []
multcols = []
print(lines)

i=0
while i < len(lines):
    if all([x == "." for x in lines[i]]):
        # lines.insert(i, ["." for x in lines[i]])
        multrows.append(i)
        # i+=1
    i+=1

i=0
while i < len(lines[0]):
    if all([x == "." for x in [line[i] for line in lines]]):
        # for line in lines:
        #     line.insert(i, ".")
        # i+=1
        multcols.append(i)
    i+=1

for line in lines:
    print("".join(line))

nodes = []
def get_neighbors(node):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if node[0] + i < 0 or node[0] + i >= len(lines):
                continue
            if node[1] + j < 0 or node[1] + j >= len(lines[0]):
                continue
            neighbors.append((node[0] + i, node[1] + j))
    return neighbors


def bfs(n1, n2):
    queue = [n1]
    visited = [n1]
    parent = {n1: None}

    while queue:
        current = queue.pop(0)
        if current == n2:
            path = []
            while current != None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                parent[neighbor] = current

def manhattan(n1, n2):
    row = n1[0]
    rowcount = 0
    while row != n2[0]:
        if row < n2[0]:
            add = 1
        else:
            add = -1
        row += add
        if row in multrows:
            add *= 1000000
        
        rowcount += add
    
    col = n1[1]
    colcount = 0
    while col != n2[1]:
        if col < n2[1]:
            add =1
        else:
            add = -1
        col += add
        if col in multcols:
            add *= 1000000
        
        colcount += add

    return abs(rowcount) + abs(colcount)


for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            nodes.append((i, j))

lengths = {}


for i in range(len(nodes)):
    for j in range(len(nodes)):
        pathlength = manhattan(nodes[i], nodes[j])
        if (j, i) not in lengths:
            lengths[(i,j)] = pathlength


print(sum([lengths[x] for x in lengths]))



