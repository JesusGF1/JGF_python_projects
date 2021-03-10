# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

html = urlopen("http://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), 'html.parser')#First argument is the HTML text the object is based on. THe second is the parser used to create the object.
#html parser is included in python, the one mostly used.
#You can use other parsers such as lxml
#pip install lxml, better and faster than html and more forgiving for messy or malformed html
#html5lib is also a nice parser, 
print(bs.h1)
"""
#These produce the same output as bs.h1
bs.html.body.h1
bs.body.h1
bs.html.h1
#These parsers can also be used
bs2 = BeautifulSoup(html, 'lxml')
bs3 = BeautifulSoup(html, 'html5lib')
"""

#Handling data exceptions

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
else:
    # program continues. Note: If you return or break in the  
    # exception catch, you do not need to use the "else" statement


    
try:
    html = urlopen('http://www.pythonscraping.com/pages/page15.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    
try:
    badContent = bs.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print ('Tag was not found')
    else:
        print(badContent)