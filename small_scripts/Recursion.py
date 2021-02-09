# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:58:35 2021

@author: jesus
"""

def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more 
                 bottles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles
             of beer. Take one down, pass it around, 
             {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(50)

def print_to_zero(n):
    if n < 0:
        return
    print(n)
    print_to_zero(n - 1)

print_to_zero(5)