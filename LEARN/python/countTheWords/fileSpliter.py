"""
Splits a text file in to words conaining 250 words each.
Removes none alphabet characters.
Takes only one parameter, the name of the file to split.

Author: Mayel Espino.
Jul 22,2017
"""
import sys
import re

if len(sys.argv) != 2 :
    print("usage: to split")
    sys.exit(1)
else:
    file = sys.argv[1]

with open(file, 'r') as textFile:
     data = textFile.read()

words = data.split()
wordCount = 0
fileCount = 0
smallFileString = ""

for index in range(len(words)):
    wordCount += 1
    wordToAdd = re.sub(r'\W+', '', words[index])
    smallFileString = "{} {} ".format(smallFileString, wordToAdd)
    if wordCount == 250:
        wordCount = 0
        fileCount += 1
        smallFile = "{}-{}".format(file,fileCount)
        print(smallFile)
        print(smallFileString)
        with open(smallFile, 'w') as textFile:
            textFile.write(smallFileString)
        smallFileString = ""
