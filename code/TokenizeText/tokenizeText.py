import re

file = open('/home/nhatnor123/Desktop/test.txt', 'r')
fileDictionary = open('/home/nhatnor123/Desktop/Dict-UTF8.txt', 'r')

example = "tinh thông khả thi Hôm nay tôi muốn đi chơi với mọi người trong lớp học của tôi vui vẻ lấp lánh"

dictionary = []

for line in fileDictionary:
    regex = "{.*?}"
    line =re.sub(re.compile(regex), "", line)
    line = line.split(" \n")[0]
    dictionary.append(line)

listWordExample = example.split(" ")
for word in listWordExample:
    print(word)

for line in dictionary:
    print(line)
    print(len(line))



def TokenizeText(listWordExample, start, end):
    for i in range(end, start-1, -1):
        tempString = ""
        for j in range(start, i + 1, 1):
            if j != i:
                tempString += listWordExample[j].lower() + "_"
            else:
                tempString += listWordExample[j].lower()

        #print(tempString)
        if tempString in dictionary:
            print(tempString)
            TokenizeText(listWordExample, i+1,end)
            break

    return None

TokenizeText(listWordExample,0, len(listWordExample)-1);