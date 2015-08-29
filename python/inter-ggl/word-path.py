#!/usr/bin/python
import re
import heapq

myDicct=["dig","dog","git","tic","tac","god","got","fig","rig","fog"]

def findPatternInDicctionary(inPattern, inDicctionary):
    m = None
    tmpSet = []
    for element in inDicctionary:
        #print "element", element
        m = re.search( "("+inPattern+")", element)
        if m :
            tmpSet.append( m.group(1))
    return tmpSet


def findCombinationsInDicctionary(inWord):
    setOfWords = []
    for index in range(len(inWord)):
        tempSetOfWords = []
        pattern = list(inWord)
        pattern[index] = '.'
        pattern = "".join(pattern)
        tempSetOfWords = findPatternInDicctionary(pattern,myDicct)
        setOfWords += tempSetOfWords
    return set(setOfWords)

firstSet = findCombinationsInDicctionary("fig")
print "firstSet",firstSet
secondSet = findCombinationsInDicctionary("dog")
print "secondSet",secondSet
intersectSet = firstSet & secondSet
print "intersectSet",intersectSet
print "Solution:"
print "Start: fig"
print "intermediate steps, select one of the following: ",intersectSet
print "End: dog"
