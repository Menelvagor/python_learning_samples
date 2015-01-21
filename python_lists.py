# python_lists.py
# Julie M. Anderson
# samples of lists in python

# Lists are heterogenous in python
 
aList = [1, 2.0, "aString", False]
print "A heterogenous list: ", aList 


# Operations on lists

sampleList = [1, 2, 3, 4]
print "My sample list: ", sampleList

# indexing using []
print "sampleList[1]: " , sampleList[1]

# concatenation using +
anotherList = ["cat", "dog"]
print "Another sample list: ", anotherList
print "sampleList + anotherList: ", sampleList + anotherList

# repetition using *
print "sampleList * 3: ", sampleList * 3

# membership using in -- checks to see if item exists in a sequence
print "4 in sampleList: ", 4 in sampleList
print "8 in sampleList: ", 8 in sampleList

# number of items in a sequence using len
print "len(anotherList): ", len(anotherList)

# slicing using [:] starts at index of first number, up to but not including second
print "sampleList: ", sampleList
print "sampleList[1:2]: ", sampleList[1:2]

# A list is a collection of references to Python data objects!

print "Be careful with lists! they are references!"
print "newList = [sampleList] * 3"
newList = [sampleList] * 3
print "newList:", newList
print "sampleList[2] = 256"
sampleList[2] = 256
print "newList: ", newList


# Built in list methods

aList = [1, 'cat', 5.0]
print "aList: ", aList

# append   aList.append(item)   Add item to end of aList
aList.append(2)
print "aList.append(2): ", aList

# insert   aList.insert(index, item)   inserts item at index
aList.insert(1, "x")
print "aList.insert(1, 'x'): ", aList

# pop   aList.pop()   removes and returns the last item 
print ".pop() removes and returns the last item."
print "aList.pop(): ", aList.pop()
print "aList: ", aList

# you can also pop at an index  aList.pop(index)
print "aList.pop(2): ", aList.pop(2)
print "aList: ", aList

# sort   aList.sort(), aList.reverse()
listToSort = [5, 12, 7, 11, 0, 3]
print "listToSort: ", listToSort
listToSort.sort()
print "listToSort.sort(): ", listToSort
listToSort.reverse()
print "listToSort.reverse(): ", listToSort

# del   del aList[index]   deletes item at index
print aList
del aList[2]
print "del aList[2]"
print "aList: ", aList

# index   aList.index(item) returns the index of the 1st occurence of the item
print "aList.index('x'): ", aList.index('x')

# count   aList.count(item) returns the number of occurrences of the item
numberList = [1] * 3
print "numberList: ", numberList
print "numberList.count(1): ", numberList.count(1)

# remove   aList.remove(item)   removes first occurrence of item
print "numberList.remove(1)"
numberList.remove(1)
print "numberList: ", numberList

