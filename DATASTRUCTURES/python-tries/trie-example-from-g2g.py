# Trie implementation in Python 
# From https://www.geeksforgeeks.org/introduction-to-trie-data-structure-and-algorithm-tutorials/

class TrieNode:
    def __init__(self):
        # pointer array for child nodes of each node
        self.childNode = [None] * 26
        self.wordCount = 0
        
def insert_key(root, key):
    # Initialize the currentNode pointer with the root node
    currentNode = root

    # Iterate across the length of the string
    for c in key:
        # Check if the node exist for the current character in the Trie.
        if not currentNode.childNode[ord(c) - ord('a')]:
            # If node for current character does not exist
            # then make a new node
            newNode = TrieNode()
            # Keep the reference for the newly created node.
            currentNode.childNode[ord(c) - ord('a')] = newNode
        # Now, move the current node pointer to the newly created node.
        currentNode = currentNode.childNode[ord(c) - ord('a')]
    # Increment the wordEndCount for the last currentNode
    # pointer this implies that there is a string ending at currentNode.
    currentNode.wordCount += 1
    
def search_key(root, key):
    # Initialize the currentNode pointer with the root node
    currentNode = root

    # Iterate across the length of the string
    for c in key:
        # Check if the node exist for the current character in the Trie.
        if not currentNode.childNode[ord(c) - ord('a')]:
            # Given word does not exist in Trie
            return False
        # Move the currentNode pointer to the already existing node for current character.
        currentNode = currentNode.childNode[ord(c) - ord('a')]

    return currentNode.wordCount > 0

def delete_key(root, word):
    currentNode = root
    lastBranchNode = None
    lastBrachChar = 'a'

    for c in word:
        if not currentNode.childNode[ord(c) - ord('a')]:
            return False
        else:
            count = 0
            for i in range(26):
                if currentNode.childNode[i]:
                    count += 1
            if count > 1:
                lastBranchNode = currentNode
                lastBrachChar = c
            currentNode = currentNode.childNode[ord(c) - ord('a')]

    count = 0
    for i in range(26):
        if currentNode.childNode[i]:
            count += 1

    # Case 1: The deleted word is a prefix of other words in Trie.
    if count > 0:
        currentNode.wordCount -= 1
        return True

    # Case 2: The deleted word shares a common prefix with other words in Trie.
    if lastBranchNode:
        lastBranchNode.childNode[ord(lastBrachChar) - ord('a')] = None
        return True
    # Case 3: The deleted word does not share any common prefix with other words in Trie.
    else:
        root.childNode[ord(word[0]) - ord('a')] = None
        return True
# Driver Code
if __name__ == '__main__':
    # Make a root node for the Trie
    root = TrieNode()

    # Stores the strings that we want to insert in the Trie
    input_strings = ["and", "ant", "do", "geek", "dad", "ball"]

    # number of insert operations in the Trie
    n = len(input_strings)

    for i in range(n):
        insert_key(root, input_strings[i])

    # Stores the strings that we want to search in the Trie
    search_query_strings = ["do", "geek", "bat"]

    # number of search operations in the Trie
    search_queries = len(search_query_strings)

    for i in range(search_queries):
        print("Query String:", search_query_strings[i])
        if search_key(root, search_query_strings[i]):
            # the queryString is present in the Trie
            print("The query string is present in the Trie")
        else:
            # the queryString is not present in the Trie
            print("The query string is not present in the Trie")

    # stores the strings that we want to delete from the Trie
    delete_query_strings = ["geek", "tea"]

    # number of delete operations from the Trie
    delete_queries = len(delete_query_strings)

    for i in range(delete_queries):
        print("Query String:", delete_query_strings[i])
        if delete_key(root, delete_query_strings[i]):
            # The queryString is successfully deleted from the Trie
            print("The query string is successfully deleted")
        else:
            # The query string is not present in the Trie
            print("The query string is not present in the Trie")

# This code is contributed by Vikram_Shirsat
