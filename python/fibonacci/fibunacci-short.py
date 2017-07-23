#!/usr/local/bin/python3

target = 10

fibb, prev = 0,1
for x in xrange(target):
    fibb, prev = prev+fibb, fibb

print(fibb)