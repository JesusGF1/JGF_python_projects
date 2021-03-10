# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 23:57:39 2021

@author: jesus
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')})
print(images)
for image in images:
    print(image['src'])
    
"""
A regular expression can be inserted as any argument in a BeautifulSoup
expression, allowing you a great deal of flexibility in finding target elements.
"""