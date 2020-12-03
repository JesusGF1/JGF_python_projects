# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:38:34 2020

@author: jesus
"""

dicc1 = {"Locus": "AT1G0408943", "Gene" : "def-3", "Protein length": 245}
dicc2 = {"Locus": "AT1G0489471", "Gene" : "fu-4", "Protein length": 278}
dicc3 = {"Locus": "AT1G0663454", "Gene" : "caca-1", "Protein length": 297}
dicc4 = {"Locus": "AT1G0788990", "Gene" : "meme", "Protein length": 323}
dicc5 = {"Locus": "AT1G0408943", "Gene" : "mono", "Protein length": 567}
lista = (dicc1, dicc2, dicc3, dicc4, dicc5)

import csv
import io

tsv = "\t".join(list(lista[0].keys()))
for dicc in lista:
    row = []  #esto lo haces para meter los elementos de dicc values como strings en una lista
    print(type(dicc.values()))
    for value in dicc.values():
        row.append(str(value))
    tsv = tsv + "\n" + "\t".join(row)
        
f = open("HOLA.tsv", "w")
f.write(tsv)
f.close()