#!/usr/bin/python
from sys import stdout

class CNode:
	L , R, data = None, None, 0    
	def __init__(self, data):
		# initializes the data members
		self.L = None
		self.R = None
		self.data = data


rootNode = CNode(10)

#       10
#     20  30
node20 = CNode(20)
node30 = CNode(30)
rootNode.L = node20
rootNode.R = node30
#       10
#     20  30
#  40   50  60
node40 = CNode(40)
node50 = CNode(50)
node60 = CNode(60)
node20.L = node40
node20.R = node50
node30.L = node50
node30.R = node60

def printwithspace(i):
    stdout.write("%i " % i)

def recursivePrint(aNode, visitor = printwithspace):
	if aNode is not None:
		visitor(aNode.data)
		#print aNode.data
		recursivePrint(aNode.L,visitor)
		recursivePrint(aNode.R,visitor)
	return

print "Starting at the root"
recursivePrint(rootNode)