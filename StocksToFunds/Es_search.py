from elasticsearch import Elasticsearch
import csv
import jieba
from collections import Counter
es = Elasticsearch([{'host':'localhost','port':9200}])

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
    for j in range(len(seg_list)):  #从后遍历 速度更快
        words_fre[seg_list[-j-1]] += 1        #添加分类词项
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

def search(name,fund_type=0):
    find = {"query": {
    "bool": {
    "must": [],
    "must_not": [ ],
    "should": [ ]
    }
    }}
    for i in name:
        temp = {"match": {"funds": ""}}
        temp["match"]["funds"] = i
        find["query"]["bool"]["must"].append(temp)
    es_answer = es.search(index="all_stocks",body=find)
    final = []
    for i in range(len(es_answer['hits']['hits'])):
        temp = es_answer['hits']['hits'][i]['_source']['stock_name']
        if fund_type!=0 and funds_dic[temp] != fund_type :
            continue
        final.append(temp)
    print("一共找到"+str(len(final))+"支基金:")
    for i in final:
        print(i)
# name = ["贵州茅台","伊利股份","五粮液","海天味业","泸州老窖","洋河股份","山西汾酒","双汇发展","中炬高新","顺鑫农业"]
name = ["长城汽车","宁德时代","比亚迪","天赐材料","泸州老窖","贵州茅台","阳光电源"]
search(name,4)  #第二个参数为指定基金类型： 1：债券 2：指数 3：股票 4：混合