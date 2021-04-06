#导入库
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pandas as pd
#创建浏览器对象
browser = webdriver.Chrome()
try:
    browser.get('http://fund.eastmoney.com/bzdm.html#os_0;isall_0;ft_;pt_1')    #设置爬取网址
    funds_list = [ [0]  for _ in range(10650)]  #创建一个二维列表 作为存储
    count = 0   #计数
    for j in range(40,55): #53  0-15 #55  爬取页数
        browser.execute_script('window.scrollBy(0,7000)')   #下滑浏览器
        
        #改用不断输入页码进行爬取
        browser.find_element_by_xpath('//*[@id="tonum"]').click()   #点击页码按钮 使其出现页码搜索框
        word = browser.find_element_by_xpath('//*[@id="tonum"]')    #点击页码搜索框 开始输入
        word.clear()    #清空页码搜索框 （避免出现上一页填写的页码仍存在）
        word.send_keys(j)   #发送页码
        browser.find_element_by_xpath('//*[@id="anim"]').click()    #点击跳转按钮

        time.sleep(1.2) #等待浏览器渲染
        num = browser.find_elements_by_css_selector('td.bg.bzdm')   #爬取基金编号 使用css_selector
        name = browser.find_elements_by_css_selector('td.tol > nobr > a:nth-child(1)')  #爬取基金名字
        url = browser.find_elements_by_css_selector('td.tol > nobr > a:nth-child(2)')   #爬取基金详细页面的url
        day_increase = browser.find_elements_by_css_selector('td.rzzl.red , td.rzzl.black , td.rzzl.green') #爬取日增长率
        service_charge = browser.find_elements_by_css_selector('td:nth-child(14)')  #爬取基金手续费
        length = len(name)
        print("第"+str(j+1)+"页")
        # print(len(num),len(name),len(url),len(day_increase),len(service_charge))
        time.sleep(0.3) #等待一下  有时候会出现错误 等待能够解决
        for i in range(length):
            funds_list[count] = [num[i].text,name[i].text,url[i].get_attribute('href'),day_increase[i].text,service_charge[i].text]     #给列表幅值  保存数据
            count += 1
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pager > span.nu.page')))    #还可以采用等待到元素加载出来为止

        #尝试循环点击下一页 但最后失败 因为一共55页太长 前面几十页都没问题 但爬到后面会出现后面的页面都是重复页面的问题 暂时不知道原因
        # browser.find_element_by_css_selector('#pager > span:nth-child(8)').click() 
        # browser.find_element_by_css_selector('#tonum').click()

    print("总长：",len(funds_list)) #统计一下数量 看数量是否足够
    # print(funds_list)

    #保存数据到excel
    dataframe = pd.DataFrame(funds_list)
    dataframe.to_csv(r'C:\Users\Administrator\Desktop\爬虫\funds_data_4.csv',encoding="utf_8_sig")
finally:
    browser.close() #关闭浏览器

# 其他3种爬虫库尝试
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
# requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
# s = requests.session()
# s.keep_alive = False # 关闭多余连接
# url="https://fund.eastmoney.com/"
# header = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'Accept-Encoding':'gzip, deflate, br',
#             'Accept-Language': 'zh-CN,zh;q=0.9',
#             'Connection':'keep-alive',
#             'Host':'same.eastmoney.com',
#             'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
#             'Referer': 'https://fund.eastmoney.com/',
#             'Upgrade-Insecure-Requests':'1'
#             }
# r=s.get(url,headers=header,allow_redirects=False)
# print(r)