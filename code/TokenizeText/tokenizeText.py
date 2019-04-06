import re
import unicodedata
import sys

# get dictionary from extenal file
fileDictionary = open('/home/nhatnor123/Desktop/Dict-UTF8.txt', 'r')
dictionary = []

for line in fileDictionary:
    if line == "### Number of part-of-speech tag: 17 ###\n":
        break;
    elif line == "### Number of words: 31137 ###\n":
        continue
    else:
        regex = "{.*?}"
        line = re.sub(re.compile(regex), "", line)
        line = line.split(" \n")[0]
        dictionary.append(line)

fileDictionary.close()


# select all word and non-word
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


# tokenize text from a ListWord
result = ""


def TokenizeText(listWordExample, start, end):
    global result
    for i in range(end, start - 1, -1):
        if i == start:
            # print(listWordExample[i],end= " ")
            result = result + listWordExample[i] + " "
            TokenizeText(listWordExample, start + 1, end)
            return
        else:
            tempString = ""
            for j in range(start, i + 1, 1):
                if j != i:
                    tempString += listWordExample[j] + "_"
            else:
                tempString += listWordExample[j]

            # print(tempString)
            if tempString.lower() in dictionary:
                # print(tempString, end= " ")
                result = result + tempString + " "
                TokenizeText(listWordExample, i + 1, end)
                return

    return None


def TokenizeTextKhuDeQuy(listWord):
    for i in range(len(listWord)):
        pass


# tokenize text from data type string
def tokenize(data):
    global result
    list = ListWord(data)
    result = ""

    symbolEndSentence = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[",
                         "]", "|", "\\", ":", ";", "'", '"', "<", ",", ".", "<", ">", "?", "/"]
    listDiemNgatCau = []

    for i in range(len(list)):
        if list[i] in symbolEndSentence:
            listDiemNgatCau.append(i)

    if len(listDiemNgatCau) == 0:
        TokenizeText(list, 0, len(list) - 1)
    else:
        TokenizeText(list, 0, listDiemNgatCau[0] - 1)

        for i in range(0, len(listDiemNgatCau), 1):
            if i == len(listDiemNgatCau) - 1:
                result = result + list[listDiemNgatCau[i]] + " "
            else:
                result = result + list[listDiemNgatCau[i]] + " "
                TokenizeText(list, listDiemNgatCau[i] + 1, listDiemNgatCau[i + 1] - 1)
        TokenizeText(list, listDiemNgatCau[len(listDiemNgatCau) - 1] + 1, len(list) - 1)

    return result


def getResultBI_Tokenize(listWordExample, start, end):
    global result
    for i in range(end, start - 1, -1):
        if i == start:
            # print(listWordExample[i],end= " ")
            result = result + "B" + " "
            getResultBI_Tokenize(listWordExample, start + 1, end)
            return
        else:
            tempString = ""
            tempBI = ""
            for j in range(start, i + 1, 1):
                if j != i:
                    tempString += listWordExample[j] + "_"
                    if j == start:
                        tempBI += "B "
                    else:
                        tempBI += "I "
            else:
                tempString += listWordExample[j]
                tempBI += "I"

            # print(tempString)
            if tempString.lower() in dictionary:
                # print(tempString, end= " ")
                result = result + tempBI + " "
                getResultBI_Tokenize(listWordExample, i + 1, end)
                return

    return None


def getResultBI_tokenize(data):
    global result
    list = ListWord(data)
    result = ""

    symbolEndSentence = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[",
                         "]", "|", "\\", ":", ";", "'", '"', "<", ",", ".", "<", ">", "?", "/"]
    listDiemNgatCau = []

    for i in range(len(list)):
        if list[i] in symbolEndSentence:
            listDiemNgatCau.append(i)

    if len(listDiemNgatCau) == 0:
        getResultBI_Tokenize(list, 0, len(list) - 1)
    else:
        getResultBI_Tokenize(list, 0, listDiemNgatCau[0] - 1)

        for i in range(0, len(listDiemNgatCau), 1):
            if i == len(listDiemNgatCau) - 1:
                result = result + "B "
            else:
                result = result + "B "
                getResultBI_Tokenize(list, listDiemNgatCau[i] + 1, listDiemNgatCau[i + 1] - 1)
        getResultBI_Tokenize(list, listDiemNgatCau[len(listDiemNgatCau) - 1] + 1, len(list) - 1)

    return result
