#!/usr/bin/python
# http://effbot.org/librarybook/random.htm

import random

listOfInts = []

def printTheList(aList):
	for i in aList:
		print i

#Populate the list with random integers.
for i in xrange(40):
	listOfInts.append(random.randint(1, 1000))


LIterator = 0
RIterator = (len(listOfInts))-1

while(LIterator < RIterator):
	#print '%d < %d' % (LIterator, RIterator)
	#Find the next even number in the bottom of the list
	while ((listOfInts[LIterator] % 2) == 0) and (LIterator < RIterator):
		#print listOfInts[LIterator]
		LIterator += 1

	#Find the next odd number in the top of the list
	#print "----"
	
	while ((listOfInts[RIterator] % 2) != 0) and (LIterator < RIterator):
		#print listOfInts[RIterator]
		RIterator -= 1

	#Now we swap them, to keep all of the odd numbers in the bottom of the list
	#And all of the even number at the top of the list
	tmp = listOfInts[LIterator]
	listOfInts[LIterator] = listOfInts[RIterator]
	listOfInts[RIterator] = tmp
	
printTheList(listOfInts)
print "LIterator %d = %d , RIterator %d = %d" %(LIterator,listOfInts[LIterator],RIterator,listOfInts[RIterator])

#Now we sort the two halfs of the list
firstHalfOfList = listOfInts[0:RIterator]
secondHalfOfList = listOfInts[LIterator:]

firstHalfOfList.sort()
printTheList(firstHalfOfList)
print "======="
secondHalfOfList.sort()
printTheList(secondHalfOfList)



