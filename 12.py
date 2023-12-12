import sys
lines = []
#import regex
import re
from functools import cmp_to_key
from math import gcd

with open('inputs/12.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))




def get_possibilities(counts, araay):
    groups = [x for x in re.split("\.+", array) if x != '']
    
    


    
    return 0
    

sum = 0
for line in lines:
    print()

    counts = [int(x) for x in line.split()[1].split(",")]
    array = line.split()[0]
    print(array)

    sum += get_possibilities(counts, array)
    # print(get_possibilities(counts, array))
    print(counts)
print(sum)