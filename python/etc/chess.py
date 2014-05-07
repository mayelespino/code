#!/usr/bin/python

import sys
import argparse



if len(sys.argv) != 3:
    print "must pass exactly 2 parameters: x y coordinate."
    exit(0) 

Xcoordinate = int(sys.argv[1])
Ycoordinate = int(sys.argv[2])


if not ( 0 < Xcoordinate <= 3):
    print "X coordinate must be grater than 1 and  must be less than 3"
    exit(0)
if not ( 0 < Ycoordinate <= 3):
    print "Y coordinate must be grater than 1 and  must be less than 3"
    exit(0)

print "Starting position: %s,%s" % (Xcoordinate, Ycoordinate)





#moves_on_board = {'1,1':'2,3|3,1|1,2|3,3', '1,2':'2,5', '1,3':'2,1|3,3', '2,1':'3,3', '2,2':'can not move 2 spaces in any direction', '2,3':'1,1|3,1|1,2|3,3', '3,1': '1,2|3,3', '3,2': '1,3|2,1|3,3'}
moves_on_board = {'1,1':'2,3', '1,2':'2,5', '1,3':'2,1|3,3', '2,1':'3,3', '2,2':'can not move 2 spaces in any direction', '2,3':'1,1|3,1|1,2|3,3', '3,1': '1,2|3,3', '3,2': '1,3|2,1|3,3'}

start =  "%s,%s" % (Xcoordinate,Ycoordinate)
print "Path to 3,3:"
print moves_on_board[start]

