from pyvi import ViTokenizer
import gensim
import operator

file = open('/home/nhatnor123/Desktop/test2.txt', 'r')
fileResult = open('/home/nhatnor123/Desktop/result.txt' , 'a')
dict = {}

for line in file:
    for word in gensim.utils.simple_preprocess(ViTokenizer.tokenize(line.lower())):
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

