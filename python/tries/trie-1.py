#!/bin/python


#
# Trie class
#
class trieNode:
    '''
    Trie class
    '''
    value = None
    mapToNodes = {}
    endOfTrie = True
    def __init__(self, value):
        self.value = value
    def addToTrieMap(self, inTrie):
        self.mapToNodes[inTrie.value] = inTrie
        self.endOfTrie = False

#
# Build a map of words (tries)
#
rootTrie = trieNode('c')
c_Trie = trieNode('c')
rootTrie.addToTrieMap(c_Trie)
d_Trie = trieNode('d')
rootTrie.addToTrieMap(d_Trie)

