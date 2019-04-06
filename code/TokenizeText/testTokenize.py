import TokenizeText.tokenizeText as tk

# data = ""
#
# file  = open('/home/nhatnor123/Desktop/test-BI.txt', 'r')
# for line in file:
#     print(line.split("\n")[0].split("\t"))
#     data += line.split("\n")[0].split("\t")[0] + " "
#
# print(data)
# # print((data.split(" ")))
# # print(len(data.split(" ")))
# result = (tk.tokenize(data))
#
# fileResult = open('/home/nhatnor123/Desktop/resultMyTk-BI.txt', 'a')
#
# fileResult.write(result)
# fileResult.close()
# file.close()

# data = """Chiều nay bạn mình thi ở D3 101 bị mất chiếc ví đen bên trong có CMT Nguyễn Trọng Cường và 1 số thẻ nữa
# Mong tìm lại được giấy, tờ còn tiền trong ví đối với bạn mình   ko quan trọng lắm """
#
# print(len(tk.getResultBI_tokenize(data).split()))
# print(len(tk.tokenize(data  ).split(" ")))

countLine = 0

resultTestTotal = 0
resultTrue = 0

resultForEachLine = []
data = ""
file = open('/home/nhatnor123/Desktop/test-BI.txt', 'r')
count = 0;
for line in file:
    countLine += 1
    print(countLine)

    if line != "\n":
        content = line.split('\n')
        resultForEachLine.append(content[0].split("\t")[1])
        data += (content[0].split("\t")[0] + " ")
    else:
        print("")
        print(data)
        print(resultForEachLine)
        result = tk.getResultBI_tokenize(data).split(" ")
        result.pop()
        print(result)

        resultTestTotal += len(result)
        k = min(len(result), len(resultForEachLine))
        for i in range(0, k):
            if resultForEachLine[i] == result[i]:
                resultTrue += 1

        print(str(resultTrue) + " / " + str(resultTestTotal))

        data = ""
        resultForEachLine.clear()
        # count += 1
        # if count == 3:
        #     break

# kết quả khi test với Test_BI là :       209383/222004 = 94.315%
