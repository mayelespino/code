#!/usr/bin/python

import fileinput

#Given an all-postive array A, find the max product from all possible trains
#train: A[i]..A[j] where i <=j
#
#A = { 1 , 3, 4, 0.9, 10 }
#i = 1
#j = 3
#A[i]..A[j] => A[1]..A[3] => A[1], A[2], A[3] = { 3, 4, 0.9 } => 3 * 4 * 0.9 = 10.8
#
#better than O(n*n)
#
#what if 0.1,0.2,0.3


def findTrain(inputArray):
	currentTrain = 0
	currentProduct = 1.0
	maxTrain = 0
	maxProduct = 0
	for item in inputArray:
		number = float(item)
		if number < 1.0:
			currentTrain += 1
			print "lessThanOne: %s" % item
			currentProduct = 1.0
		print "currentTrain: %s, currentProduct: %s, number: %s" % (currentTrain,currentProduct,number)
		currentProduct *= number
		if currentProduct > maxProduct:
			maxProduct = currentProduct
			maxTrain = currentTrain
		
	return(maxProduct,maxTrain)

# getting the input from < afile.txt
########################################################
# Main
########################################################
for line in fileinput.input():
	print line
	
	numberArray = line.split(',')
	(product,trainNo) = findTrain(numberArray)
	print product,trainNo
	
	
# My original solution (sucks :)
#
#    endOfArray = len(input)
#    train[] = {}
#    train[0] = 0
#    trainNo = 0    
#    for index in range(endOfArray):
#        if input[index] < 1 :
#            trainNo += 1
#            train[trainNo] = 0
#        else:
#            train[trainNo] = input[index] * train[trainNo]    
#    maxProduct = 0
#    maxTraiNo = 0
#    for index in range(endOfArray):
#        if maxProduct < train[index]:
#            maxProduct = train[index]
#            maxTrainNo = index    
