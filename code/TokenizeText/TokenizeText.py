import re
import unicodedata
import sys


#get dictionary from extenal file
fileDictionary = open('/home/nhatnor123/Desktop/Dict-UTF8.txt', 'r')
dictionary = []

for line in fileDictionary:
    if line == "### Number of part-of-speech tag: 17 ###\n" :
        break;
    elif line == "### Number of words: 31137 ###\n" :
        continue
    else :
        regex = "{.*?}"
        line = re.sub(re.compile(regex), "", line)
        line = line.split(" \n")[0]
        dictionary.append(line)

fileDictionary.close()



#select all word and non-word
def ListWord(text):
    text = unicodedata.normalize('NFC', text)

    specials = ["==>", "->", "\.\.\.", ">>"]
    digit = "\d+([\.,_]\d+)+"
    email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    datetime = [
        "\d{1,2}\/\d{1,2}(\/\d+)?",
        "\d{1,2}-\d{1,2}(-\d+)?",
    ]
    word = "\w+"
    non_word = "[^\w\s]"
    abbreviations = [
        "[A-ZĐ]+\.",
        "Tp\.",
        "Mr\.", "Mrs\.", "Ms\.",
        "Dr\.", "ThS\."
    ]

    patterns = []
    patterns.extend(abbreviations)
    patterns.extend(specials)
    patterns.extend([web, email])
    patterns.extend(datetime)
    patterns.extend([digit, non_word, word])

    patterns = "(" + "|".join(patterns) + ")"
    if sys.version_info < (3, 0):
        patterns = patterns.decode('utf-8')
    tokens = re.findall(patterns, text, re.UNICODE)
    listWord = []
    for set in tokens:
        listWord.append(set[0])
    return listWord



#tokenize text from a ListWord
result = ""

def TokenizeText(listWordExample, start, end):
    global result
    for i in range(end, start - 1, -1):
        if i==start:
            #print(listWordExample[i],end= " ")
            result = result + listWordExample[i]+" "
            TokenizeText(listWordExample, start+1, end)
            return
        else :
            tempString = ""
            for j in range(start, i + 1, 1):
                 if j != i:
                     tempString += listWordExample[j] + "_"
            else:
                 tempString += listWordExample[j]

            #print(tempString)
            if tempString.lower() in dictionary:
                #print(tempString, end= " ")
                result = result + tempString+" "
                TokenizeText(listWordExample, i + 1, end)
                return

    return None



#tokenize text from data type string
def Tokenize(data):
    global result
    list = ListWord(data)
    result = ""
    TokenizeText(list, 0, len(list)-1)
    return result




xau = "heello chúng m lấp lánh sao đỏ cờ vàng áo vàng quần áo bộ trưởng"
print(Tokenize(xau))


