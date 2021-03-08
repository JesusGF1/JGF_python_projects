# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 09:53:33 2021

@author: jesus
"""
#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd



#%% Per possesion dataframe for each player
url ='https://www.basketball-reference.com/players/d/doncilu01.html'
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
tabla = pd.read_html(str(bs.find("div", {'id':'all_per_poss'})).replace("<!--", ""))[0]



#%%
url="https://www.basketball-reference.com/teams/"
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
print(bs.find("div", {'id':'div_teams_active'}))
tabla = pd.read_html(str(bs.find("div", {'id':'div_teams_active'})))[0] #Tabla con datos generales sobre los equipos

#%% url of the teams
#print(bs.find("div", {'id':'div_teams_active'}).findAll("a"))
teams = bs.find("div", {'id':'div_teams_active'}).findAll("a")

print([team.get("href") for team in teams])

#%%
urlteam = "https://www.basketball-reference.com/teams/ATL/"
html = urlopen(urlteam)
bs = BeautifulSoup(html, 'html.parser')
print(bs.find("div", {'id':'div_ATL'}).find("a").get("href")) #with this I find the last season


#print(bs.find("div", {'id':'div_ATL'}))

#%% scraping players webpages
url = "https://www.basketball-reference.com/teams/ATL/2021.html"
html = urlopen(url)
bs = BeautifulSoup(html, 'html.parser')
print(bs.find("table", {'id':'roster'}).findAll("td", {"data-stat":"player"}))
players = bs.find("table", {'id':'roster'}).findAll("td", {"data-stat":"player"})
print([player.find("a").get("href") for player in players])

#%%
print([tag.name for tag in bs.find_all()])