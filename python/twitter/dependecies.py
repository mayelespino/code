#!/usr/bin/python
import fileinput
from collections import defaultdict

#
# Read the dependencies from the command line. program < input.txt
#
print "Read the input file..."
dependencyTable = defaultdict(list)
for line in fileinput.input():
	line = line.rstrip()
	print line
	parts = line.split('=')
	fileName = parts[0]
	dependencies = parts[1].split(',')
	for dependency in dependencies:
		print dependency
		dependencyTable[fileName].append(dependency)

print "Done reading the file."

def printDependencies(fileName):
	for dependency in  dependencyTable[fileName]:
			print dependency

def printReverseDependecies(fileName):
	for key,value in dependencyTable.iteritems():
		if fileName in value:
			print key

print "Printing depenencies of file 'e' "
printDependencies('e')
print "Printing reverse dependencies of 'd'"
printReverseDependecies('d')

'''
This is the original implementation I did, copy pasted from collabedit.

#dep[A]=b,c
#rdep[F]=D

#dep[D]=E,F
#rdep[D]=B


#ddep = {}
#rdep = {}


# Data comes from:
#getEdges()
#Yields (primary, dependent) tuples


for each line in getEdges():
    primary,dependent = line
    createDependencies(primary,dependent)

def createDependecies(primary,dependent):
    deplist = ddep[primary]
    if deplist = None:
        deplist = []
        deplist.append(primary)
        ddep[primary] = deplist
       
    if not hasA(deplist,primary):
        deplist.append(primary)
        ddep[primary] = deplist
    
    deplist /Similar...
    
    
def printDependencies(node):
    print "Direct dependencies for:%s\n" % node
    dependencies = ddep[node]
    foreach item in dependencies:
        print "%s " % item
        
   print "Reverse dependencies  for:%s\n" % node
    dependencies = rdep[node]
    foreach item in dependencies:
        print "%s " % item
'''