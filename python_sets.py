# python_sets.py
# JM Anderson
# Sample of sets in Python

# A set in Python is an unordered group of immutable Python data objects
# A set cannot have duplicates
# An empty set is written set()
# sets are heterogenous

emptySet = set()
print "An Empty Set is written set(): ", emptySet

print 'aSet = {1, 5.0, "x", True}'
aSet = {1, 5.0, "x", True}
print "aSet: "
print aSet

# in works on sets
print "'x' in aSet: ", 'x' in aSet

# len returns cardinality of the set
print "len(aSet): ", len(aSet)

# set operations:
setOne = {1, 2, 3, 4, 5}
setTwo = {2, 4, 6}
print "setOne: ", setOne
print"setTwo: ", setTwo

# |   setOne | setTwo   returns a new set with elements from both sets
print "setOne | setTwo: ", setOne | setTwo

# &   setOne & SetTwo   returns new set with common elements
print "setOne & setTwo: ", setOne & setTwo

# -    setOne - setTwo   returns a new set with all items from first set not in second set
print "setOne - setTwo: ", setOne - setTwo

# <=   setOne <= setTwo   asks whether all elements of first set are in second set
print "setOne <= setTwo: ", setOne <= setTwo



# set methods

# union   setOne.union(setTwo)   returns a new set with all elements from both sets
print "setOne.union(setTwo): ", setOne.union(setTwo)

# intersection    setOne.intersection(setTwo) returns a new set with only common elements
print "setOne.intersection(setTwo): ", setOne.intersection(setTwo)

# difference   setOne.difference(setTwo)   returns a new set with all items from first 
#											set not in second set
print "setOne.difference(setTwo): ", setOne.difference(setTwo)

# issubset   setOne.issubset(setTwo)  returns True if all items in set one are in set two
print "setOne.issubset(setTwo): ", setOne.issubset(setTwo)


# items can be added and removed from a set, but not changed via index
# use add, remove, pop and clear
print "aSet = {1, 2, 3, 4, 5}"
aSet = {1, 2, 3, 4, 5}

aSet.add(6)
print "aSet.add(6): ", aSet

aSet.remove(3)
print "aSet.remove(3): ", aSet

print "aSet.pop(): ", aSet.pop()
print "aSet: ", aSet

aSet.clear()
print "aSet.clear(): ", aSet

