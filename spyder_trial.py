#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://home.nanjing.fang.com/zhuangxiu/DealerList_192_0_0_0_0_3_0_1_/'
#URL = 'http://www.sina.com.cn'
r = requests.get(URL)
print(r.status_code)
r.encoding = 'gbk'
print(r.encoding)
html = r.text

soup = BeautifulSoup(html, 'html.parser')

print(soup.title.string)

content = soup.body.find('div', class_ = 'shop_cont').find_all('ul')
print(len(content))
csv_header = ['name', 'about', 'address']
csv_rows=[]
for item in content:
    csv_rows.append({
    'name': item.b.a.string,
    'about': item.p.string,
    'address': item.find(text = '查看地图').find_parent().find_parent().get('address')
    })
    #print(item.find(text = '查看地图').find_parent().find_parent())
#print(csv_rows)

with open('crm_fang.csv','w', encoding='utf-8') as f:
    f_csv = csv.DictWriter(f, csv_header)
    f_csv.writeheader()
    f_csv.writerows(csv_rows)
'''
file = open("trial.html", "wb")
file.write(str(content[0]).encode('gb18030'))
file.close()
'''
