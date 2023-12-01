import sys
f = open('inputs/1.txt', 'r')
lines = f.read().splitlines()

def getFirstDigit(line):
    for i in range(0, len(line)):
        if isNumeric(line[i]):
            return int(line[i])
        
def getLastDigit(line):
    for i in range(len(line)-1, -1, -1):
        if isNumeric(line[i]):
            return int(line[i])

def isNumeric(char):
    try:
        int(char)
        return True
    except ValueError:
        return False
    

def getFirstWord(string):
    replacements = {
        "nine": "9",
        "eight": "8",
        "seven": "7",
        "six": "6",
        "five": "5",
        "four": "4",
        "three": "3",
        "two": "2",
        "one": "1",
    }
    minword = ""
    minindex = 100000000
    for key in replacements.keys():
        if key in string:
            if string.index(key) < minindex:
                minindex = string.index(key)
                minword = key
    if minword == "":
        return None
    
    #if theres a number before the word, return None
    for i in range(0, minindex):
        if isNumeric(string[i]):
            return None
    return minword

def getLastWord(string):
    replacements = {
        "nine": "9",
        "eight": "8",
        "seven": "7",
        "six": "6",
        "five": "5",
        "four": "4",
        "three": "3",
        "two": "2",
        "one": "1"
    }
    maxword = ""
    maxindex = -1
    for key in replacements.keys():
        if key in string:
            if string.rfind(key) > maxindex:
                maxindex = string.rfind(key)
                maxword = key
    if maxword == "":
        return None
    return maxword




def replaceNums(someString):

    word = getFirstWord(someString)
    word2 = getLastWord(someString)
    replacements = {
        "nine": "9",
        "eight": "8",
        "seven": "7",
        "six": "6",
        "five": "5",
        "four": "4",
        "three": "3",
        "two": "2",
        "one": "1"
    }
    new = someString
    if word != None:

        
        new = new.replace(word, replacements[word], 1)
    if word2 != None:
        new = new[::-1]

        new = new.replace(word2[::-1], replacements[word2][::-1], 1)
        new = new[::-1]

       
        
    
    # string = string.replace("zero", "0")
    return new



# print(lines)
sum = 0
for i in range(0, len(lines)):
    print(lines[i])
    correct = replaceNums(lines[i])
    print(correct)
    print()
    first = getFirstDigit(correct)
    last = getLastDigit(correct)
    both = int(str(first) + str(last))
    sum += both


print (sum)


