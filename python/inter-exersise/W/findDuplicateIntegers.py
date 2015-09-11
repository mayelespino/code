#!/usr/bin/python
"""
Find the duplicates integers in a large array. Array with integers from 1-1,000,000.

Author: Mayel Espino
"""
import random

sizeOfArray =100000
maxInteger = 1000000

arrayOfIntegers = [random.randint(1, maxInteger) for r in xrange(sizeOfArray)]
summaryHash = {}


def isDuplicate(number):
    if summaryHash.get(number, None) is not None:
        summaryHash[number] += 1
        return number
    else:
        summaryHash[number] = 0

map(isDuplicate, arrayOfIntegers)


print "Number - occurrences"
for key, value in summaryHash.items():
    if value != 0:
        print key, value


# NOTE:
# I considered the approach of comparing the sum of the array of integers to the expected sum of integer, to find the
# duplicates. The problem with this approach is that it does not account for multiple numbers being repeated or multiple
# times.