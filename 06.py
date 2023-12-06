import sys
lines = []

with open('inputs/06.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

times = lines[0].split(":")[1].replace(" ", "").split()
distances = lines[1].split(":")[1].replace(" ", "").split()

mult=1
for (i,time) in enumerate(times):
    tobeat = int(distances[i])
    count=0
    for t in range(0, int(time)):
        speed = t
        dst = t*(int(time)-t)
        if dst >= int(tobeat):
            count+=1
    mult*=count
    



print(mult)
print(times)
print(distances)