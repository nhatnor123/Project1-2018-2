import re
import unicodedata
import sys



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



def TokenizeText(listWordExample, start, end):
    for i in range(end, start - 1, -1):
        if i==start:
            print(listWordExample[i].lower())
            TokenizeText(listWordExample, start+1, end)
        else :
            tempString = ""
            for j in range(start, i + 1, 1):
                 if j != i:
                     tempString += listWordExample[j].lower() + "_"
            else:
                 tempString += listWordExample[j].lower()

            #print(tempString)
            if tempString in dictionary:
                print(tempString)
                TokenizeText(listWordExample, i + 1, end)
                break

    return None




file = open('/home/nhatnor123/Desktop/test.txt', 'r')
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



example = "tinh thông khả thi Hôm nay tôi muốn đi chơi với mọi người trong lớp học của tôi vui vẻ lấp lánh"
example2 = "tinh ,thông khả fskdjfklj vãi cả lồn địt mẹ hay :))) Hôm nay tôi muốn đi chơi với   công ty tnhh mtv Nguyễn lưu nhật mọi người trong lớp học của tôi đây là đài tiếng nói Việt NaMM   , ....."


print(dictionary)

print(ListWord(example2))

TokenizeText (ListWord(example2), 0, len(ListWord(example2)) - 1 )

print(len(ListWord(example)))
print(len(ListWord(example2)))

fileDictionary.close()
file.close()