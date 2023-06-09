from structlinks.DataStructures import BinarySearchTree
bst = BinarySearchTree.create_tree([1, 2, 4, 5, 6, 7, 8])
print(bst)

from binarytree import Node
root = Node(3)
root.left = Node(6)
root.right = Node(8)

# Getting binary tree
print('Binary tree :', root)

# Getting list of nodes
print('List of nodes :', list(root))

# Getting inorder of nodes
print('Inorder of nodes :', root.inorder)

# Checking tree properties
print('Size of tree :', root.size)
print('Height of tree :', root.height)

# Get all properties at once
print('Properties of tree : \n', root.properties)

                                                                                                                                                                                            

# https://pypi.org/project/structlinks/
# https://github.com/eeshannarula29/structlinks/tree/main/DataStructures/Stack
# https://github.com/eeshannarula29/structlinks/tree/main/DataStructures/Queue
# https://www.geeksforgeeks.org/binarytree-module-in-python/