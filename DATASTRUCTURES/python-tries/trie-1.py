#
# Trie class
#
class trieNode():
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = trieNode()

    def addWords(self, wordList):
        for word in wordList:
#            self.addWord(word)
            self.insert(word)

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:  # If it does not exist add it
                node.children[char] = trieNode()
            node = node.children[char]  # If it does, go to it's childNode
        node.end = True

    def findWord(self, word):
        trieIter = self.root
        for char in word:
            if char in trieIter.children:  # If it does not exist, go to it's childNode
                trieIter = trieIter.children[char]
            else:
                return False
        return trieIter.end

    def _walk_trie(self, node, word, word_list):

        if node.children:
            for char in node.children:
                word_new = word + char
                if node.children[char].end:
                    word_list.append(word_new)
                self._walk_trie(node.children[char], word_new, word_list)

    def autoComplete(self, partial_word):
        node = self.root

        word_list = []
        # find the node for last char of word
        for char in partial_word:
            if char in node.children:
                node = node.children[char]
            else:
                # partial_word not found return
                return word_list

        if node.children:
            word_list.append(partial_word)

        #  word_list will be created in this method for suggestions that start with partial_word
        self._walk_trie(node, partial_word, word_list)
        return word_list


# create a Trie

t = Trie()
words = ['hi', 'hieght', 'rat', 'ram', 'rattle', 'hill']
t.addWords(words)

print("Search for word")
words = ['hi', 'hello', 'ra','hieght', 'rat', 'ram', 'rattle', 'hill' ]
for word in  words:
   print(word, t.findWord(word))

# print("search for words using prefix -  auto complete")
print(t.autoComplete('ra'))
