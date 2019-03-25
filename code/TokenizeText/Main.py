import TokenizeText.tokenizeText as tk

import gensim
import operator

file = open('/home/nhatnor123/Desktop/test.txt', 'r')

dict = {}

for line in file:
    data = tk.tokenize(line)
    print(data)
    for word in gensim.utils.simple_preprocess(data.lower()):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

#for key in dict:
    #print(key+" : "+ str(dict[key]))

for line in sorted(dict.items(), key= operator.itemgetter(1)) :
    print(line)

#test : test 6613 line : 12p


file.close()