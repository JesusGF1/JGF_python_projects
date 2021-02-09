# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:20:19 2021

@author: jesus
"""

integers = [1,2,3,1,3]

def find_unique(integerlist):
    diccounts = {}
    for i in integerlist:
        if i in diccounts:
            diccounts[i] += 1
        else:
            diccounts[i] = 1
    for k in diccounts:
        if  diccounts[k] == 1:
            return k

print(find_unique(integers))    