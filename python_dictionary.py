# python_dictionary.py
# JM Anderson
# Samples of Python dictionaries

# Python dictionaries are unordered collections of key:value pairs.
# aDict = {'key1':'value1', 'key2':'value2"}

# Keys are used to access values much like the index in a sequence.

capitals = {'Illinois':'Springfield', 'Wisconsin':'Madison'}
print "capitals = {'Illinois':'Springfield', 'Wisconsin':'Madison'}"

# access a value using the key.
print "capitals['Illinois']"
print capitals['Illinois']

# add a key:value pair
capitals['California'] = 'Sacramento'
print "capitals['California'] = 'Sacramento'"
print "print capitals"
print capitals

# use len() to find number of key:value pairs
print "len(capitals):  ", len(capitals)

# iterate over a dictionary
print '''
for k in capitals:	
	print capitals[k], "is the capital of ", k'''
for k in capitals:
	print capitals[k], "is the capital of ", k
	
# list operators include [], in, and del

# []   aDict[key]   Returns the value associated with k and an error if key does not
# 						exist in the list.
print "capitals['Illinois']"
print capitals['Illinois']

# in   key in aDict    returns bool
print "'Alaska' in capitals: ", 'Alaska' in capitals

# del   del aDict[key]   removes key:value pair at key
print "del capitals['California']"
del capitals['California']
print capitals


# methods for dictionaries in Python

aDict = {'cat':1, 'dog':2, 'fish':3}
print "aDict: ", aDict

# keys   aDict.keys()   Returns the keys of a dictionary
print "aDict.keys()"
print aDict.keys()

# values  aDict.values()  Returns the values of a dictionary
print "aDict.values()"
print aDict.values()

# items   aDict.items()   Returns the key:value pairs 
print "aDict.items()"
print aDict.items()

# get   aDict.get(key)  Returns the value associated with key, None if key is not in dict
#       aDict.get(key, alt)  same as above but returns alt if key is not in dict
print "aDict.get('dog')"
print aDict.get('dog')
print "aDict.get('lion', 'NO!')"
print aDict.get('lion', 'NO!')


 
  
	



