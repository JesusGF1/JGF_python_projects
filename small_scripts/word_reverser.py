# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:49:14 2021

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

def word_reverser(word):
    stacker = Stack()
    for letter in word:
        stacker.push(letter)
        #print(stacker.peek())
    reversedword = []
    while stacker.size() > 0:
        reversedword += stacker.pop()
    print("".join(reversedword))

word_reverser("patata")