# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:03:46 2021

@author: jesus
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

def list_reverser(lista):
    stacker = Stack()
    for item in lista:
        stacker.push(item)
        #print(stacker.peek())
        
    reversedlist = []
    while stacker.size() > 0:
        reversedlist.append(stacker.pop())
    print(reversedlist)
lista = [1,2,3,4,5]
list_reverser(lista)