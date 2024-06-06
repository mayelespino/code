#/usr/bin/python

print "Singly linked list"
print "Start."

class Node:
	nextNode = 0
	data = 0
	
first = Node()
first.data = "first node"

second = Node()
second.data = "second node"
first.nextNode = second

iterator = first
print iterator.data
while iterator.nextNode:
		iterator = iterator.nextNode
		print iterator.data
		
nodeArray = []

print "Create an array of nodes"
for index in xrange(10):
	nodeArray.append(Node())

print "Fill the array of Nodes with data and build the link list"
for index in xrange(9):
	nodeArray[index].data = index
	nodeArray[index].nextNode = nodeArray[index+1]
nodeArray[9].data = 9

print "Print the list."
iterator = nodeArray[0]
while iterator.nextNode != 0:
	print iterator.data
	iterator = iterator.nextNode
print iterator.data

print "Remove the node that has data 1 from the list."
iterator = nodeArray[0]
while iterator.data != 5:
	preTargetNode = iterator
	iterator = iterator.nextNode
print "Found ", iterator.data
targetNode = iterator
preTargetNode.nextNode = iterator.nextNode

print "Print the list."
iterator = nodeArray[0]
while iterator.nextNode != 0:
	print iterator.data
	iterator = iterator.nextNode
print iterator.data

print "Finish."
