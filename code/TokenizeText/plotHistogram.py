import pandas as pd
import matplotlib.pyplot as plt

class PlotHistogram():
    #reload(sys)
    #sys.setdefaultencoding('utf8')
    histogram = {}
    f = open('/home/nhatnor123/Desktop/3.txt')
    for x in range(20):
        (word, count) = next(f).split(' : ')
        histogram[word] = int(count)
    f.close()
    df = pd.DataFrame.from_dict(histogram, orient='index')
    df.plot(kind='bar')
    plt.show()