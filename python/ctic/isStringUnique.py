#!/usr/bin/python
import string
import random

isUnique = True
stringLenght = 20
randomString = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(stringLenght))
print randomString

for index in range(stringLenght-1):
    if randomString[index] in randomString[index+1:]:
        print 'Found ',randomString[index], 'duplicated'
        isUnique = False
        //TODO: break out of loop if one letter is repeated

print 'return',isUnique