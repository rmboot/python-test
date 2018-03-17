# -*- coding: utf-8 -*-
import xlwt
import requests
from bs4 import BeautifulSoup
wbk = xlwt.Workbook()
my = wbk.add_sheet('my')
res=requests.get("https://rmboot.com/")
res.encoding="utf8"
soup=BeautifulSoup(res.text,"lxml")
a=soup.select("a")
n=0
for i in a:
    if(i.text and i.get("href")):
        my.write(n,0,i.text)
        my.write(n,1,i.get("href"))
        n=n+1
wbk.save('E:/Uploads/test.xls')
