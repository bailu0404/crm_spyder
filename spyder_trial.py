#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

#URL = 'http://home.nanjing.fang.com/zhuangxiu/DealerList_192_0_0_0_0_3_0_1_/'
URL = 'http://www.sina.com.cn'
r = requests.get(URL)
print(r.status_code)
print(r.encoding)
html = r.text

soup = BeautifulSoup(html, 'html.parser')

print(soup.head.encode('gb2312'))


'''
file = open("trial.html", "wb")
file.write(r.text.encode('utf-8'))
file.close()
'''
