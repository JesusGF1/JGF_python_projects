# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:05:33 2021

@author: jesus
"""

"""Web scraping"""

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getSiteHTML(url):    
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
    except AttributeError as e:
        return None
    return(bs.html)
"""
webpage = getSiteHTML('https://news.google.com/topstories?hl=es-419&gl=US&ceid=US:es-419')
if webpage == None:
    print('Webpage could not be found')
else:
    print(webpage)
"""
