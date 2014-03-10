#!/usr/bin/python
# Problem statement:
# Given a long list of sentences (containing letters from the English alphabet and spaces) determine for each sentence in 
# the list whether it contains all the letters in the alphabet or not. The input sentences are read from the standard 
# input, separated by newlines. After processing each sentence output a "y" if the sentence contains all the letters # 
# in the alphabet and "n" otherwise to the standard output.
#
# Sample call:
# localhost:~ $ solution1 < problem1_sentences.txt
#
import fileinput

#
# Search for all the characters in the range 'A' to 'Z'.
# Return TRUE only if ALL of the characters were found
# in the input string provided, at least once.
# Return FALSE otherwise.
#
def hasUpCase(inputLine):
	for charNo in range(65,91):
		if chr(charNo) not in line:
			return False
	return True

#
# Search for all the characters in the range 'a' to 'z'.
# Return TRUE only if ALL of the characters were found
# in the input string provided, at least once.
# Return FALSE otherwise.
#
def hasLowCase(inputLine):
	for charNo in range(97,123):
		if chr(charNo) not in line:
			return False
	return True
	
########################################################
# Start of program
########################################################	
for line in fileinput.input():
	hasAllCaps = hasUpCase(line)
	hasAllLows = hasLowCase(line)
	if hasAllCaps or hasAllLows:
		print "Y"
	else:
		print "N"
			
exit(0)