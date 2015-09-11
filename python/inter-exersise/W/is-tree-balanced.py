#!/usr/bin/python
"""
Given a binary tree, determine if the tree is balance.

Author: Mayel Espino
"""

from collections import namedtuple
import Queue

Node = namedtuple('Node', 'data, left, right')

T1N6 = Node('6', None, None)
T1N5 = Node('5',None, None)
T1N4 = Node('4',None, None)
T1N3 = Node('3',None, None)
T1N2 = Node('2', T1N5, T1N6)
T1N1 = Node('1', T1N3, T1N4)
balancedTree = Node('0', T1N1, T1N2)

T2N8 = Node('8', None, None)
T2N7 = Node('7', None, None)
T2N6 = Node('6', T2N7, T2N8)
T2N5 = Node('5', None, None)
T2N4 = Node('4',None, None)
T2N3 = Node('3',None, None)
T2N2 = Node('2', T2N5, T2N6)
T2N1 = Node('1', T2N3, T2N4)
unBalancedTree = Node('0', T2N1, T2N2)

T3N4 = Node('4',None, None)
T3N3 = Node('3',T3N4, None)
T3N2 = Node('2', None, None)
T3N1 = Node('1', T3N2, T3N3)
unBalancedTree_two = Node('0', T3N1, T3N2)

T4N2 = Node('2', None, None)
T4N1 = Node('1', None, None)
balancedTree_two = Node('0', T4N1, T4N2)


childCountQueue = Queue.Queue()

def traverseTree(node):
    if node is not None:
        numberOfChildren = 0
        print node.data,
        # if node.left is not None:
        #     numberOfChildren =+ 1
        # if node.right is not None:
        #     numberOfChildren =+ 1
        if node.left is not None and node.right is not None:
            numberOfChildren = 2
        elif node.left is None and node.right is None:
            numberOfChildren = 0
        else:
            numberOfChildren = 1
        childCountQueue.put(numberOfChildren)
        traverseTree(node.left)
        traverseTree(node.right)

def isTreeBalanced(inTree):
    traverseTree(inTree)
    treeIsBalanced = True
    while not childCountQueue.empty():
        nodeCount = childCountQueue.get()
        print nodeCount
        if nodeCount == 0:
            nodeCount = childCountQueue.get()
            print nodeCount
            if nodeCount != 0:
                 treeIsBalanced = False

    if treeIsBalanced:
        print "Tree is balanced."
    else:
        print "Tree NOT balanced."

    return

    # while not childCountQueue.empty():
    #     print childCountQueue.get()
    # return

print 'traverseTree1: ',
isTreeBalanced(balancedTree)


print '\ntraverseTree2: ',
isTreeBalanced(unBalancedTree)


print '\ntraverseTree3: ',
isTreeBalanced(unBalancedTree_two)

print '\ntraverseTree4: ',
isTreeBalanced(balancedTree_two)
