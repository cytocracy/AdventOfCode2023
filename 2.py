import sys
f = open('inputs/2.txt', 'r')
lines = f.read().splitlines()

sum = 0
i=0
for line in lines:
    i += 1
    canmake = True
    content = line.split(": ")[1]
    grabs = content.split("; ")
    for grab in grabs:
        colors = grab.split(", ")
        for color in colors:
            things = color.split(" ")
            num = int(things[0])
            name = things[1]
            print(num)
            print(name)
            print()
            if name == 'blue':
                if num > 14:
                    canmake = False
            elif name == 'red':
                if num > 12:
                    canmake = False
            elif name == 'green':
                if num > 13:
                    canmake = False
    if canmake:
        sum += i

sum2 = 0
for line in lines:
    i += 1
    canmake = True
    content = line.split(": ")[1]
    grabs = content.split("; ")
    minred = 0
    mingreen = 0
    minblue = 0
    for grab in grabs:
        colors = grab.split(", ")
        for color in colors:
            things = color.split(" ")
            num = int(things[0])
            name = things[1]
            print(num)
            print(name)
            print()
            if name == 'blue':
                if num > minblue:
                    minblue = num
            elif name == 'red':
                if num > minred:
                    minred = num
            elif name == 'green':
                if num > mingreen:
                    mingreen = num
    add = minred * mingreen * minblue
    sum2 += add


print(sum2)


