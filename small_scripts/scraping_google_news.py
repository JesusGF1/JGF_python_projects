# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:12:47 2021

@author: jesus
"""

"Scraping google news"

import re
import web_scrapper as ws


url = "https://www.instagram.com/irenepenaalva/?hl=es"
webpage = ws.getSiteHTML(url)

print(webpage)
#webpage.type
#x = re.findall("https://.+,", webpage)