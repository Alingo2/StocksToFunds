from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
import csv
error = []
def get_stocks(fund,url):
    stock_list = 41*[0] #预先建立储存列表
    stock_list[0] = fund
    count = 1
    browser.get(url)
    stocks = browser.find_elements_by_xpath('//*[@id="position_shares"]/div[1]/table/tbody/tr/td[1]/*') #查找股票建仓
    portion1 = browser.find_elements_by_xpath('//*[@id="position_shares"]/div[1]/table/tbody/tr/td[2]') #查找股票建仓比例
    l1,l2 = len(stocks),len(portion1)
    if l1 == l2:
        for i in range(len(stocks)):
            stock_list[count] = stocks[i].text   #不用append 提高效率
            stock_list[count+1] = portion1[i].text
            count += 2
    else:
        print(l1,l2,'股票数据条数不等！')
        error.append((fund,url))
    # time.sleep(0.1)
    browser.execute_script('window.scrollBy(0,700)')
    browser.find_element_by_xpath('//*[@id="quotationItem_DataTable"]/div[1]/div[2]/h3/a').click()
    bonds = browser.find_elements_by_xpath('//*[@id="position_bonds"]/div[1]/table/tbody/tr/td[1]') #查找债券建仓
    portion2 = browser.find_elements_by_xpath('//*[@id="position_bonds"]/div[1]/table/tbody/tr/td[2]')#查找债券建仓比例
    l3,l4 = len(bonds),len(portion2)
    if l3 == l4:
        for i in range(l3):
            stock_list[count] = bonds[i].text
            stock_list[count+1] = portion2[i].text
            count += 2
    else:
        print(l3,l4,'债券数据条数不等！')
        error.append((fund,url))
    # print(stock_list)
    return stock_list

#读取基金详细页面网址
funds_list = []
with open(r'C:\Users\Administrator\Desktop\爬虫\funds_data.csv',encoding="utf-8")as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        funds_list.append([row[2],row[3]])
#创建模拟浏览器
global browser
browser = webdriver.Chrome()
total_length = len(funds_list)
fund_stock_table = [[0] for _ in range(total_length)]       #创建2维数组
#遍历调用爬取函数
for i in range(1,total_length):
    print('第',i,'条:',funds_list[i][0])
    fund_stock_table[i-1] = get_stocks(funds_list[i][0],funds_list[i][1])
browser.close()
# print(fund_stock_table)
print(error)    #打印爬取出错条数
#保存数据
dataframe = pd.DataFrame(fund_stock_table)
dataframe.to_csv(r'C:\Users\Administrator\Desktop\爬虫\funds_stock_table.csv',encoding="utf_8_sig")