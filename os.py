#! /usr/bin/python
#coding=utf-8
import sys
import os
import requests
from bs4 import BeautifulSoup  

header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
re = requests.get("http://www.ifeng.com",headers=header)
soup = BeautifulSoup(re.text, "html.parser")
co = soup.prettify()
# print(co)
f = open("index.html","w",)
f.write(co)
f.close()
print("写入完成")

