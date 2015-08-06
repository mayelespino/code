__author__ = 'mayelespino'

import random

def generateMatrix(inMatrix):
    longestRowSize = 0
    depth = random.randint(1,5)
    width = random.randint(1,5)
    for d in xrange(1,depth):
        newRow = [random.randint(1,100) for r in xrange(width)]
        inMatrix.append(newRow)
    depth -= 1
    return (depth, width)

def printMatrixRegular(inMatrix):
    if len(inMatrix) < 1:
        print "nothing to print regular"

    for row in inMatrix:
        print row

def checkCoordinate(inMatrix, inRow, inCol):
    validCoordinate =  True
    try:
        inMatrix[inRow][inCol]
    except:
        validCoordinate = False
    return validCoordinate

def printTheDiagonalSequence(inSequence):
    print "now printing in a bell curve format."
    for element in inSequence:
        print element,

def printMatrixDiagonal(inMatrix, inDepth, inWidth):
    if len(inMatrix) < 1:
        print "nothing to print diagonal"

    diagonalSequence = []
    if inDepth == 1 or inWidth == 1:
        print "Diagonal sequence: "
        for value in inMatrix:
            print value,
        return

    totalItems = inDepth * inWidth
    baseRow = 0
    baseCol = 1
    R = 0
    C = 0


    print "Diagonal sequence: "
    for index in xrange(1,totalItems):
        try:
            value = inMatrix[R][C]
        except:
            #print ".",
            if C < (inWidth - 1):
                baseCol += 1
                baseRow = 0

            if baseRow >= (inDepth -1):
                baseRow = 0

            R = baseRow
            C = baseCol
            value = inMatrix[R][C]

        print value,
        diagonalSequence.append(value)

        if R == 0 and C == 0:
            R = 0
            C = 1
        else:
            R +=1
            C -=1

        if C == -1:
            baseCol += 1
            R = baseRow
            C = baseCol

        if baseCol >= inWidth:
            baseRow += 1
            baseCol = inWidth - 1
            R = baseRow
            C = baseCol

    R = inDepth - 1
    C = inWidth - 1
    value = inMatrix[R][C]
    print value
    diagonalSequence.append(value)
    printTheDiagonalSequence(diagonalSequence)
#
#
#

myMatrix = []
(depth, width) = generateMatrix(myMatrix)
print "---"
printMatrixRegular(myMatrix)
print "---"
printMatrixDiagonal(myMatrix,depth,width)

