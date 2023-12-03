import sys
lines = []

with open('inputs/03.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n") + ".")


def isNumeric(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

def getNeighbors(pts):
    neighbors = []
    for pt in pts: #pt = (row, col)
        x = pt[0]
        y = pt[1]
        neighbors.append((x-1, y-1))
        neighbors.append((x-1, y))
        neighbors.append((x-1, y+1))
        neighbors.append((x, y-1))
        neighbors.append((x, y+1))
        neighbors.append((x+1, y-1))
        neighbors.append((x+1, y))
        neighbors.append((x+1, y+1))
    return set(neighbors)


row = 0

nums = []
symbols = []
indexes = []
gears = []
gearvals = {}
gearnums = {}
for line in lines:
    #get nums and coords of nums
    row +=1
    currNum = ''
    
    currindex = 0
    for i in range(len(line)):
        col = i+1
        
        if line[i] != '.':
            if not isNumeric(line[i]):
                symbols.append((row, col))
                if line[i] == "*":
                    gears.append((row, col))
                if currNum != '':
                    nums.append((currNum, row, currindex))
                # indexes.append((row, currindex))
                    currNum = ''
            else:
                if currNum == '':
                    currindex = col
                currNum += line[i]
        else:
            if line[i] == '.' and currNum != '':
                nums.append((currNum, row, currindex))
                # indexes.append((row, currindex))
                currNum = ''

     

print(nums)
print(symbols)

sum=0

for num in nums:
    val = int(num[0])
    x = num[1]
    y = num[2]
    
   
    pts = []
    length = len(str(val))
    for j in range(length):
        # print(x, y+j)
        pts.append((x, y+j))
    neighbors = getNeighbors(pts)
    # print(neighbors)
    did_get = False
    for coord in neighbors:
        if coord in gears:
            if coord not in gearvals:
                gearvals[coord] = val
                gearnums[coord] = 1
            else:
                gearnums[coord] += 1
                gearvals[coord] *= val
        if coord in symbols:
            if not did_get:
                sum += val
            did_get = True

    if not did_get:
        pass
        # print(val, x, y)

sum2 = 0
for key in gearnums:
    if gearnums[key] == 2:
        sum2 += gearvals[key]
    

    


print(sum)
print(sum2)