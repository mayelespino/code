#!/usr/bin/python
import re
str = 'an example word:dog!!'
match = re.search(r'word:\w+', str)
# If-statement after search() tests if it succeeded
if match:                      
	print 'found', match.group() ## 'found word:cat'
else:
	print 'did not find'
	
str = raw_input("Gime me a string : ")
match = re.search(r'^([-|+])?\d+(.)?\d+$',str)
if match:                      
	print 'found', match.group() 
else:
	print 'did not find'
