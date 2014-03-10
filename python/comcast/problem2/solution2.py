#!/usr/bin/python
#Problem statement:
# Given a text document determine whether it contains at least one sentence from a known set of sentences. 
# Assume that the sentences contain only words separated by white spaces. A sentence is contained in the 
# text document if it contains the words in the sentence as consecutive tokens (ignoring white spaces between 
# words in both the text and the sentences) with no punctuation mark between the tokens. Note that the 
# contained sentence does not need to match a sentence in the document, it can be contained in it. The document 
# is given as a text file and the set of sentences as a file containing sentences separated by newlines. 
# Use preprocessing of the known sentences freely.
#
# Sample call:
# solution2.py problem2_sentences.txt problem2_document.txt
#
import sys
import re

#
# Search for each word in a give sentence with in a given line of a document.
# If all the words of a sentence are contained in the line, return True.
# Return false otherwise.
#
def searchForSentece(inLine, inSentence):
	#print "[%s]\n" % inLine
	#print "   >%s<" % inSentence
	words = inSentence.split(' ')
	for word in words:
		if word not in inLine:
			return False
	return True


########################################################
# Start of program
#######################################################

# Check the arguments provided
if len(sys.argv) != 3:
	print "Must provide two file names: first a sentences file, second a document file, in the command line."
	exit(1)

# Read the files
sentencesFile = sys.argv[1]
documentFile = sys.argv[2]

print "sentences File: " + sentencesFile
sentences = [line.strip() for line in open(sentencesFile)]

	
print "document File: " + documentFile
documentData = ""
with open (documentFile, "r") as docfile:
	documentData=docfile.read().replace('\n', '')

# Regular expression pattern to tokenise the document in to an array.
pattern = re.compile(r"[.,;]")
documentArray = pattern.split(documentData)

# Search through each line of the document for each word in the sentences give. 
# Print the sentences found and the line were they were found.
for line in documentArray:
	for sentence in sentences:
		if searchForSentece(line,sentence):
			print "Found sentence [%s] contained in document, in line [%s].\n" % (sentence, line)

exit(0)