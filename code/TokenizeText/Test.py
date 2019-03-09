from pyvi import ViTokenizer
import gensim

file = open('/home/nhatnor123/Desktop/test.txt', 'r')

dict = {}

for line in file:
    for word in gensim.utils.simple_preprocess(ViTokenizer.tokenize(line.lower())):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

for key in dict:
    print(key+" : "+ str(dict[key]))

file.close()

