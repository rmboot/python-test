# -*- coding: utf-8 -*-
import re
import requests
import pymysql.cursors
from bs4 import BeautifulSoup
#获取数据库连接
con=pymysql.connect(host="localhost",user="root",password="12345678",
                    db="spider",charset="utf8mb4")
siteres=requests.get("http://www.yinwang.org")
siteres.encoding="utf8"
sitesoup=BeautifulSoup(siteres.text,"lxml")
a=sitesoup.find_all("a",href=re.compile(r"^/blog-cn/"))
for i in a:
    url="http://www.yinwang.org"+i.get('href')
    res=requests.get(url)
    res.encoding="utf8"
    soup=BeautifulSoup(res.text,"lxml")
    title=soup.find("h2").text
    content=""
    contentli=soup.find_all(["h3","p"])
    for li in contentli:
        content=content+li.text+"\n"
    with con.cursor() as cursor:#获取会话指针
        sql='INSERT INTO news (title,content,url) VALUES (%s,%s,%s)'
        cursor.execute(sql,(title,content,url))
        con.commit()#提交
    print(url)
