from elasticsearch import Elasticsearch
import json
import csv
es = Elasticsearch([{'host':'localhost','port':9200}])      
num = 0
with open(r'C:\Users\Administrator\Desktop\爬虫\funds_stock_table.csv', 'r',encoding="utf-8") as f:
    f_csv = csv.reader(f)   
    for row in f_csv:
        funds = []
        for i in range(2,len(row)-1,2): #步长为2 读入基金名称 股票名称
            funds.append((row[i],row[i+1]))
        data = {                        #数据格式
            "stock_name" : row[1],
            "funds" :funds,
        }
        res = es.index(index="all_stocks", doc_type="doc", body=data)   #添加进入Es
        num += 1    #计数
        print(num)