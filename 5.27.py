# -*- coding: utf-8 -*-
"""
Created on Thu May 27 13:14:07 2021

@author: sunyi
"""

import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,0,6);
while 1==1:
    time.sleep(second);
    html=urlopen(
        "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98").read().decode('utf-8')

    naver=BeautifulSoup(html,features='lxml')
    # text=naver.find('div',{'class','news_area'})
    text=naver.find_all('a',{'class','news_tit'}) 
    for m in text:
        print(m.get_text())
        