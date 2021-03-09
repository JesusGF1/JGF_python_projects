# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 11:09:07 2021

@author: jesus
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
#import re
import pandas as pd
import time

domain = "https://www.basketball-reference.com"

def scraping_actual_team_players(team_abbreviation):
    """ Aqui metes abreviacion y te devuelve lista con las tablas"""
    starting_point = domain + "/teams/"
    teamurl = starting_point + team_abbreviation + "/"
    team_id = "div_" + team_abbreviation
    html = urlopen(teamurl)
    bs = BeautifulSoup(html, 'html.parser')
    actual_team_url = domain + str(bs.find("div", {'id': team_id}).find("a").get("href"))
    html = urlopen(actual_team_url)
    bs = BeautifulSoup(html, 'html.parser')
    players = bs.find("table", {'id':'roster'}).findAll("td", {"data-stat":"player"})
    players_url = [player.find("a").get("href") for player in players]
    team_players_list = []
    for player_url in players_url:
        time.sleep(3)
        url = domain + player_url
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        print(player_url)
        try:
            tabla = pd.read_html(str(bs.find("div", {'id':'all_per_poss'})).replace("<!--", ""))[0]        
            tabla["Player"] = bs.find("h1", {"itemprop" : "name"}).text.strip()
            indice = tabla[tabla["Season"]=="Career"].index[0]
            tabla = tabla[0:indice]
            tabla = tabla.drop(axis= 1,columns = "Unnamed: 29")
            #no me encuentra tablas para uno del college que es el darlina01
            print(player_url)
            team_players_list.append(tabla)
        except:
            pass
    return pd.concat(team_players_list)

Tabla_equipo = scraping_actual_team_players("LAL")


def scraping_league_stats():
    """Scraping the entirety of the teamplayers"""
    url="https://www.basketball-reference.com/teams/"
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    teams = bs.find("div", {'id':'div_teams_active'}).findAll("a")
    teams_url = [team.get("href") for team in teams]
    team_players_list = []
    for team in teams_url:
        time.sleep(3)
        teamurl = domain + team
        print(teamurl) #fafaf
        html = urlopen(teamurl)
        bs = BeautifulSoup(html, 'html.parser')
        div_team = "div_" + teamurl[-4:-1]
        season = bs.find("div", {'id':div_team}).find("a").get("href") #tengo que cambiarlo para que este guay
        #esto tiene la URL de la ultima season
        seasonurl = domain + season
        print(seasonurl)
        html = urlopen(seasonurl)
        bs = BeautifulSoup(html, 'html.parser')
        players = bs.find("table", {'id':'roster'}).findAll("td", {"data-stat":"player"})
        player_url_list = [player.find("a").get("href") for player in players]
        for player in player_url_list:
            player_url = domain + player
            time.sleep(3)
            print(player_url)
            html = urlopen(player_url)
            bs = BeautifulSoup(html, 'html.parser')
            try:
                tabla = pd.read_html(str(bs.find("div", {'id':'all_per_poss'})).replace("<!--", ""))[0]        
                tabla["Player"] = bs.find("h1", {"itemprop" : "name"}).text.strip()
                indice = tabla[tabla["Season"]=="Career"].index[0]
                tabla = tabla[0:indice]
                tabla = tabla.drop(axis= 1,columns = "Unnamed: 29")
                #no me encuentra tablas para uno del college que es el darlina01
                print(player_url)
                team_players_list.append(tabla)
            except:
                pass
    return pd.concat(team_players_list)
            
    
    
Tabla_NBA = scraping_league_stats()    
    
Tabla_NBA.to_csv("NBA.csv")
#pd.concat(list)

#string = "https://www.basketball-reference.com/teams/BOS/"
