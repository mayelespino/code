#!/usr/bin/python

from collections import namedtuple
from sys import stdout


Node = namedtuple('Node', 'data, left, right')
N6 = Node('6', None, None)
N5 = Node('5',None, None)
N4 = Node('4',None, None)
N3 = Node('3',None, None)
N2 = Node('2', N5, N6)
N1 = Node('1', N3, N4)
tree = Node('0', N1, N2)


def preorder(node):
    if node is not None:
        stdout.write("%s " % node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node is not None:
        inorder(node.left)
        stdout.write("%s " % node.data)
        inorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        stdout.write("%s " % node.data)

def levelorder(node, more=None):
    if node is not None:
        if more is None:
            more = []
        more += [node.left, node.right]
        stdout.write("%s " % node.data)
    if more:
        levelorder(more[0], more[1:])

stdout.write('  preorder: ')
preorder(tree)
stdout.write('\n   inorder: ')
inorder(tree)
stdout.write('\n postorder: ')
postorder(tree)
stdout.write('\nlevelorder: ')
levelorder(tree)
stdout.write('\n')