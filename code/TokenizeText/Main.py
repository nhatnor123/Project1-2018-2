import tokenizeText as tk

import gensim
import operator

file = open('/home/nhatnor123/Desktop/test.txt', 'r')

dict = {}

for line in file:
    for word in gensim.utils.simple_preprocess(tk.Tokenize(line.lower())):
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1

#for key in dict:
    #print(key+" : "+ str(dict[key]))

for line in sorted(dict.items(), key= operator.itemgetter(1)) :
    print(line)
