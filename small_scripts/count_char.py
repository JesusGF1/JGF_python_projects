# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:59:04 2021

@author: jesus
"""

def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)