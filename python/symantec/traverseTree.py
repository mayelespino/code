#!/usr/bin/python
#from http://rosettacode.org/wiki/Tree_traversal#Python

from collections import namedtuple
from sys import stdout

#                  1
#             2         3
#           4   5    6   11
#          7 12    8   9 
#
Node = namedtuple('Node', 'data, left, right')
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      Node(12,None, None)),
                 Node(5, Node(12,None, None)
										, Node(8,None, None))),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 Node(11,
										Node(9,None,None)
										, None)))

Total = 0
def printwithspace(i):
    stdout.write("%i " % i)
 
def preorder(node, visitor = printwithspace):
    if node is not None:
        visitor(node.data)
        preorder(node.left, visitor)
        preorder(node.right, visitor)

def levelorder(node, more=None, visitor = printwithspace):
	if node is not None:
		Total =+ node.data
		print "[%d]" % Total
		if more is None:
			more = []
		more += [node.left, node.right]
		visitor(node.data)
		if more:
			levelorder(more[0], more[1:], visitor)
		

stdout.write('  preorder: ')
#preorder(tree)
levelorder(tree)
