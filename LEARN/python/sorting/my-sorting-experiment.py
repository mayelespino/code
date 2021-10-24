from random import randint

listOfRandomInts = []
for x in xrange(0,5):
    listOfRandomInts.append(randint(0,99))

def sort(inputList):

    if len(inputList) == 1:
        return (inputList)
    elif len(inputList) == 2:
        if inputList[0] < inputList[1]:
            return(inputList)
        else:
            tmpList = []
            tmpList[0] = inputList[1]
            tmpList[1] = inputList[0]
            return(tmpList)


    aList = inputList[:len(inputList) / 2]
    aList = sort(aList)
    if len(aList) > 1:
        aList = sort(aList)

    bList = inputList[len(inputList) / 2:]
    bList = sort(bList)
    if len(bList) > 1:
        bList = sort(bList)

    if aList[0] < bList[0]:
        return(aList+bList)
    else:
        return(bList+aList)


sortedList = sort(listOfRandomInts)
print listOfRandomInts
print sortedList