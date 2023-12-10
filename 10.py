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

for (i, line) in enumerate(lines):
    for (j, char) in enumerate(line):
        tiles[(i, j)] = char
        if char == ".":
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

print((len(bfs(fakestart, fakeend))+1)/2)





# print(neighbors)