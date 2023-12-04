import sys
lines = []

with open('inputs/04.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

counts = {
    n: 1 for n in range(len(lines))
}
sum=0
for (i, line) in enumerate(lines):
    print("i: " + str(i))

    # print(line)
    nums = line.split(": ")[1]
    have = nums.split(" | ")[1]
    # have.strip()
    havenums = have.split(" ")
    havenums = [x.strip() for x in havenums]
    havenums = [x for x in havenums if x != '']
    if " " in havenums:
        
        havenums.remove(" ")
    print(havenums)
    need = nums.split(" | ")[0]
    # print(neednums)
    neednums = need.split(" ")
    if " " in neednums:
        neednums.remove(" ")

    count = 0
    for num in havenums:
        if num in neednums:
            # print("num: " + num)
            count += 1

    # cardindex = i+1

    winningnumbers = count
    print("winningnumbers: " + str(winningnumbers))
    countthis = counts[i]
    for position in range(i+1, i+winningnumbers+1):
        print("added " + str(countthis) + " to card" + str(position))
        counts[position] += countthis
    print(count)
    print()
    # for winning in range(counts[i]):
    #     for position in range(i+1, count+1):
    #         print("added to card" + str(position))
    #         counts[position] += counts[i]

    if count > 0 :
        sum += 2**(count-1)
        # print((2**(count-1)))
    else:
        sum += count
    # print(sum)

#sum values of counts
sum2=0
for key in counts:
    sum2 += counts[key]



print(sum2)
# print(counts)