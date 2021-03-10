# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:42:13 2021

@author: jesus
"""

import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://www.upm.es/").text
                    
soup = bs(page, "html.parser")
print(soup.findAll("div", class_ = "cabecera"))

###Post le metes info a la web para que te envie información que no te enviaria
#si no le metes nada. Como las forms de clustal etc.

#get aparece en el URL
#Post tienes los inputs que hay que llenar para que salga bien
#los posts tienen ids que hay que llamar