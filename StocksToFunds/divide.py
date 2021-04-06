import csv
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

funds_all = []
with open(r'C:\Users\Administrator\Desktop\爬虫\funds_data.csv', 'r',encoding="utf-8") as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        funds_all.append(row[2])

bond_funds = []
index_funds = []
stock_funds = []
# currency_funds = []
mix_funds = []
divide_list = []
all_words = ""
funds_dic = {}
words_fre = Counter()
jieba.add_word("定开")
for i in range(len(funds_all)):
    seg_list = jieba.lcut(funds_all[i])    #返回列表
    words = " ".join(seg_list)    #分词后插入空格
    all_words = all_words + " " + words
    divide_list.append(words)
    funds_dic[funds_all[i]] = 0
    # temp = "/".join(seg_list)
    # print(temp)
    for j in range(len(seg_list)):  #从后遍历
        words_fre[seg_list[-j-1]] += 1
        if seg_list[-j-1] == "债券":
            bond_funds.append(i)
            funds_dic[funds_all[i]] = 1
            break
        if seg_list[-j-1] == "指数":
            index_funds.append(i)
            funds_dic[funds_all[i]] = 2
            break
        if seg_list[-j-1] == "股票":
            stock_funds.append(i)
            funds_dic[funds_all[i]] = 3
            break
        if seg_list[-j-1] == "混合":
            mix_funds.append(i)
            funds_dic[funds_all[i]] = 4
            break

for (k,v) in words_fre.most_common(100):
  print('%s%s %s %d' % (' '*(5-len(k)), k, '*'*int(v/20), v))
wordcloud = WordCloud(font_path="simkai.ttf",background_color="white",width=800, height=660).generate(all_words)  #生成词云
wordcloud.to_file(r'C:\Users\Administrator\Desktop\pic.png')     #保存图片

# for i in range(len(funds_all)):
#     if funds_dic[funds_all[i]] == 0:
#         print(funds_all[i])

# print(funds_dic)
# print(count_list)
# a = len(bond_funds)
# b = len(index_funds)
# c = len(stock_funds)
# e = len(mix_funds)
# print(bond_funds)
# print(index_funds)
# print(stock_funds)
# print(mix_funds)
# print(a,b,c,e,a+b+c+e)

bond_funds_A = []
bond_funds_B = []
bond_funds_C = []

stock_funds_A = []
stock_funds_B = []

currency_funds_A = []
currency_funds_B = []

mix_funds_A = []
mix_funds_B = []

