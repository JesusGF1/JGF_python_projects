# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 19:57:46 2021

@author: jesus
"""
#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('span', {'class':'green'})

print(nameList)

for name in nameList:
    print(name.get_text())
    
"""
.get_text() strips all tags from the document you are working with and returns
a Unicode string containing the text only. For example, if you are working with
a large block of text that contains many hyperlinks, paragraphs, and other tags,
all those will be stripped away, and you’ll be left with a tagless block of text.
Keep in mind that it’s much easier to find what you’re looking for in a
BeautifulSoup object than in a block of text. Calling .get_text() should
always be the last thing you do, immediately before you print, store, or
manipulate your final data. In general, you should try to preserve the tag
structure of a document as long as possible.
"""

"""
find_all(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
"""

#%%%
#bs.findAll and bs.find
"""
The tag argument is one that you’ve seen before; you can pass a string name
of a tag or even a Python list of string tag names. For example, the following
returns a list of all the header tags in a document:1
"""
tagslist = bs.find_all(['h1','h2','h3','h4','h5','h6'])
print(tagslist)

#%%
"""
The attributes argument takes a Python dictionary of attributes and
matches tags that contain any one of those attributes. For example, the
following function would return both the green and red span tags in the
HTML document:
"""
bothgreenandred = bs.find_all('span', {'class':{'green', 'red'}})
print(bothgreenandred)

"""
The recursive argument is a boolean. How deeply into the document do you
want to go? If recursive is set to True, the find_all function looks into
children, and children’s children, for tags that match your parameters. If it is
False, it will look only at the top-level tags in your document. By default,
find_all works recursively (recursive is set to True); it’s generally a good
idea to leave this as is, unless you really know what you need to do and
"""
#%%%
"""
The text argument is unusual in that it matches based on the text content of
the tags, rather than properties of the tags themselves. For instance, if you
want to find the number of times “the prince” is surrounded by tags on the
example page, you could replace your .find_all() function in the previous
example with the following lines:
"""
nameList = bs.find_all(text='the prince')
print(len(nameList))
"""
The limit argument, of course, is used only in the find_all method; find is
equivalent to the same find_all call, with a limit of 1. You might set this if
you’re interested only in retrieving the first x items from the page. Be aware,
however, that this gives you the first items on the page in the order that they
occur, not necessarily the first ones that you want.
"""
#%%
"""
The keyword argument allows you to select tags that contain a particular
attribute or set of attributes. For example:
"""
title = bs.find_all(id='title', class_='text')
print(title)

"""
In addition, you might occasionally run into problems using keyword, most notably
when searching for elements by their class attribute, because class is a protected
keyword in Python. That is, class is a reserved word in Python that cannot be used as
a variable or argument name (no relation to the BeautifulSoup.find_all() keyword
argument, previously discussed).2 For example, if you try the following call, you’ll get
a syntax error due to the nonstandard use of class:
"""
bs.find_all(class='green') #It does not work
bs.find_all(class_='green') #It works
bs.find_all('', {'class':'green'}) #It works

"""
Recall that passing a list of tags to .find_all() via the attributes list acts as
an “or” filter (it selects a list of all tags that have tag1, tag2, or tag3...). If
you have a lengthy list of tags, you can end up with a lot of stuff you don’t
want. The keyword argument allows you to add an additional “and” filter to
this.
"""

#BeautifoulSoup objects
"""
Beautifoul soup objects
Tag objects (bs.div.h1)
NavigableString objects 
Comment object
"""
#%%%
#Navigating trees
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
#print(bs.h1)
#print(bs.tr)
print(bs.div.table.tr)
"""
For example, the
tr tags are children of the table tag, whereas tr, th, td, img, and span are all
descendants of the table tag (at least in our example page). All children are
descendants, but not all descendants are children.
"""

#%%
#If you want to find only descendants that are children, you can use the
#.children tag:
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)

#%%
#Dealing with siblings
#The BeautifulSoup next_siblings() function makes it trivial to collect data
#from tables, especially ones with title rows:
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)



