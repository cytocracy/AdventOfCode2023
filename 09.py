import sys
lines = []
#import regex
import re
from functools import cmp_to_key
from math import gcd

with open('inputs/09.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))



sum = 0
def getval(history):

    if all([x == history[0] for x in history]):
        return history[0]
    else:
        difflist = [history[i] - history[i-1] for i in range(1, len(history))]
        return history[-1] + getval(difflist)
    
def getfirstval(history):
    if all([x == history[0] for x in history]):
        return history[0]
    else:
        difflist = [history[i] - history[i-1] for i in range(1, len(history))]
        return history[0] - getfirstval(difflist)
    

for line in lines:
    history = [int(x) for x in line.split()]
    print(getfirstval(history))
    sum += getfirstval(history)

print(sum)
    
