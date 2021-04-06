import pandas as pd
import json
import csv

data = {}
with open(r'C:\Users\Administrator\Desktop\爬虫\funds_stock_table.csv', 'r',encoding="utf-8") as f:
    f_csv = csv.reader(f)   #读入文件
    for row in f_csv:
        temp = {row[1]:{}}
        for i in range(2,len(row)-1,2): #步长为2
            name = str(row[i])
            temp[row[1]][row[i]]=row[i+1]
        # print(temp)
        data[row[0]] = temp
with open(r'C:\Users\Administrator\Desktop\爬虫\funds_stock_table.json', 'w',encoding="utf-8") as f:    #保存文件为json
    json.dump(data,f,ensure_ascii=False)