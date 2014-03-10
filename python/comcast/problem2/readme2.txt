Problem 2
* There is no need to compile this program, it's a python program.

* How to call it :
localhost:~ $solution2.py problem2_sentences.txt problem2_document.txt

* The main idea of the solution:
As I understand it the requirement is that the words in the prase are contained in consecutive words (sentence or paragraph with no punctuation marks) in the document. Not an exact match, but rather that all the words are contained in the document sentence/paragraph: "Note that the contained sentence does not need to match a sentence in the document, it can be contained in it."

The approach I took is to:
1.- "tokenize" the document in to sentences/paragraphs (containing no punctuation marks).
2.- search in each sentence/paragraph from the document, for each phrase given.
2.1.- for each phrase, "tokenize" in to words.
2.2.- using the "in" function in Python, search for each word in the phrase in the document's sentence/paragraph.
2.3.- Return True if all the words in the phrase were found in the sentece/paragraph (in no particular order), return False otherwise.

-- Mayel Espino ><>