from pyvi import ViTokenizer

# import gensim
# import operator
#
# file = open('/home/nhatnor123/Desktop/test.txt', 'r')
#
# dict = {}
#
# for line in file:
#     for word in gensim.utils.simple_preprocess(ViTokenizer.tokenize(line.lower())):
#         if word not in dict:
#             dict[word] = 1
#         else:
#             dict[word] += 1
#
# #for key in dict:
#     #print(key+" : "+ str(dict[key]))
#
# for line in sorted(dict.items(), key= operator.itemgetter(1)) :
#     print(line)
#
#
#
# file.close()

print(ViTokenizer.tokenize("tinh ,thông nhatnor123@gmail.com khả thi Hôm nay tôi muốn đi chơi với kfjslkjf lksjdfl ji  công ty tnhh mtv Nguyễn lưu nhật mọi người trong lớp học của tôi    , ..... /^ &^ vui      vẻ lấp       lánh"))

print(ViTokenizer.tokenize("nhatnor123@gmail.com là địa chỉ mail của tôi. tôi là Nguyễn Lưu Nhật, đại học bách khoa, http://www.facebook.com.vn"))
print(ViTokenizer.tokenize("Học sinh học sinh vật học "))
