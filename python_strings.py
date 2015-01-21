# python_strings.py
# JM Anderson
# Samples of strings in Python

# Strings in Python are sequences of letters, numbers and symbols(characters)       
# use single or double quotes to differentiate strings 

# Strings are immutable!!! You cannot change an item in a list using indexing.

# All sequence operations work on strings [], +, *, in, len, [:]

# String built in methods

aString = "The quick brown fox jumps over the lazy dog."
print "aString: ", aString

# count   aString.count(item)   returns number of occurrences of item in aString

print "aString.count('o'): ", aString.count('o')

# lower   aString.lower()   returns a string in all lowercase
print "aString.lower(): ", aString.lower()

# upper   aString.lower()   returns a string in all uppercase
print "aString.upper(): ", aString.upper()

# find   aString.find(item)   returns the index of the first occurrence of item
print "aString.find('q'): ", aString.find('q')

#split   aString.split(schar)   splits string into substrings at schar
print "aString.split(' '): ", aString.split(' ')

# formatting strings format a string in a field of a certain width:
littleString = 'hi'

print "littleString: ", littleString
print "littleString.center(30): "
print littleString.center(30)
print "littleString.ljust(30): "
print littleString.ljust(30)
print "littleStrin.rjust(30): "
print littleString.rjust(30)

