#!/usr/bin/python
#https://docs.python.org/2/tutorial/datastructures.html

#---- filter ----
print "---- filter ----"
def isEven(x): return x % 2 == 0
        
myList = (filter(isEven, range(1,20)))
for N in myList:
    print N

#---- map ----
print "---- map ----"

seq1 = range(1,10)
seq2 = range(101,110)

def addThem(x, y): return x+y

myList = (map(addThem, seq1, seq2))
for N in myList:
    print N

#---- reduce ----
print "---- reduce ----"

def addThem(x, y): return x+y
seq = range(1,10)
print seq
print (reduce(addThem, seq ))
