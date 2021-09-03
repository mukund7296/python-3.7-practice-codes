# A Python program to show different ways to create
# Counter
from collections import Counter

# With sequence of items 
lst=['B','B','A','B','C','A','B','B','A','C']

print(Counter(lst))

from collections import ChainMap


d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

print(c)


import collections

# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
dic3 = { 'f' : 5 }

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap using map
print ("All the ChainMap contents are : ")
print (chain.maps)

