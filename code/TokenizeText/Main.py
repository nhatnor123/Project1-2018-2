import TokenizeText.tokenizeText as tk
import TokenizeText.plotHistogram as plotHis
import gensim
import operator

file = open('/home/nhatnor123/Desktop/test1.txt', 'r')
fileResult = open('/home/nhatnor123/Desktop/result1.txt' , 'a')
dict = {}

for line in file:
    data = tk.tokenize(line)
    print(data)
    for word in gensim.utils.simple_preprocess(data.lower()):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

for x, y in sorted(dict.items(), key= operator.itemgetter(1), reverse=True) :
    print(x, end=" : ")
    print(y)
    fileResult.write(x+" : "+ str(y)+"\n")

file.close()
fileResult.close()

dictory = '/home/nhatnor123/Desktop/result1.txt'
plotHis.PlotHistogram(dictory)
