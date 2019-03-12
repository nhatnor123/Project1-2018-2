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



def TokenizeText(listWordExample, start, end, result):
    for i in range(end, start - 1, -1):
        if i==start:
            print(listWordExample[i],end= " ")
            result = result + listWordExample[i]+" "
            TokenizeText(listWordExample, start+1, end, result)
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
                print(tempString, end= " ")
                result = result + tempString+" "
                TokenizeText(listWordExample, i + 1, end, result)
                return

    return None



def tokenize(data):
    list = ListWord(data)
    result = ""
    TokenizeText(list, 0, len(list)-1, result)
    return result





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





example1 = "tinh thông khả thi Hôm nay tôi  "
example2 = "tinh ,thông khả fskdjfklj vãi cả  hay :))) Hôm nay tôi muốn đi chơi với  nhatnor123@gmail.com  công ty tnhh mtv Nguyễn lưu nhật mọi người trong lớp học của tôi đây là đài tiếng nói Việt NaMM   , ....."
example3 = " 'đừng vễ trễ ' 13h ngày 24/2, tổ tuần tra trên cao tốc Nội Bài - Lào Cai phát hiện một xe Innova 7 chỗ dừng tại làn khẩn cấp tại km 236+250 thuộc xã Gia Phú, Bảo Thắng, tỉnh Lào Cai. Đằng sau xe, 6 người đang trải chiếu ngồi ăn uống."
example4 = "'phó văn phòng', 'phó tiến sĩ' nhatnor123@gmail.com , 'dài đuồn đuỗn', 'lãnh sự quán', 'kí túc xá', 'keo tai tượng', 'bom từ trường', 'cực chẳng đã', 'giày bát kết', 'ngắn tun hủn', 'quốc tế ca', 'hoa mép dê', 'tẻo tèo teo', 'óc bã đậu"

print(ListWord(example2))

TokenizeText (ListWord(example3), 0, len(ListWord(example3)) - 1, "" )



print(tokenize(example1))