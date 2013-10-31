#coding=UTF-8
from bs4 import BeautifulSoup

doc = ['<html><head><link type="text/css" src="main.css"/><head>',
       '<body>',
       '<img src="main.png">',
       '<p>中文</p></body></html>']

soup = BeautifulSoup(''.join(doc))
print soup.prettify()
