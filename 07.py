import sys
lines = []
#import regex
import re
from functools import cmp_to_key

with open('inputs/07.txt') as f:
    for line in f.readlines():
        lines.append(line.strip("\r\n"))

FIVEOFKIND = 1
FOUROFKIND = 2
FULLHOUSE = 3
THREEOFKIND = 4
TWOPAIR = 5
ONEPAIR = 6
HIGHCARD = 7


typemap = {
    1: "five of a kind",
    2: "four of a kind",
    3: "full house",
    4: "three of a kind",
    5: "two pair",
    6: "one pair",
    7: "high card"
}

hands = []


nummap = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

def getJvalue(hand):
    jindex = hand.index(1)
    #get most common char other than 1
    #if tie then get higher char
    counts = set([(char, hand.count(char)) for char in hand if char != 1])
    maxcount = (0, 0)
    for count in counts:
        if count[1] > maxcount[1]:
            maxcount = count
        elif count[1] == maxcount[1]:
            if count[0] > maxcount[0]:
                maxcount = count
    
    return maxcount[0]
    


def checkchars(char, hand):
    return hand.count(char)

def gettype(hand):

    localhand = hand.copy()
    if 1 in localhand:
        for i in range(len(localhand)):
            if localhand[i] == 1:
                localhand[i] = getJvalue(localhand)

    #if five of a kind
    if localhand[0] == localhand[1] == localhand[2] == localhand[3] == localhand[4]:
        return FIVEOFKIND
    
    if len(set(localhand)) == 2:
        if localhand.count(localhand[0]) == 1 or localhand.count(localhand[0]) == 4:
            #four of a kind
            return FOUROFKIND
        else:
            #full house
            return FULLHOUSE
    if len(set(localhand)) == 3:
        
        for char in localhand:
            if localhand.count(char) == 3:
                #three of a kind
                return THREEOFKIND
        return TWOPAIR
    if len(set(localhand)) == 4:
        #one pair
        return ONEPAIR
    if len(set(localhand)) == 5:
        #high card
        return HIGHCARD

    #if full house

def compare(hand1, hand2):
    if gettype(hand1[0]) < gettype(hand2[0]):
        return 1
    elif gettype(hand1[0]) > gettype(hand2[0]):
        return -1
    else:
        i = 0
        while hand1[0][i] == hand2[0][i]:
            i += 1
        if hand1[0][i] > hand2[0][i]:
            return 1
        else:
            return -1


count = 0
for line in lines:
    hand = line.split()[0]
    bet = line.split()[1]
    numhand = [nummap[x] for x in hand]
    

    print(numhand)
    hands.append((numhand, bet))

for hand in hands:
    print(hand, typemap[gettype(hand[0])])
    

hands = sorted(hands, key=cmp_to_key(compare), reverse=False)

# print(hands)
i=1
while i <= len(hands):
    hand = hands[i-1]
    print(hand)
    print('i: ', i, 'bet: ', hand[1])
    count += i * int(hand[1])
    i+=1

print(count)