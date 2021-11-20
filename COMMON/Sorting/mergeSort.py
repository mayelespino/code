from random import randint

def mergeSort(list):
    if len(list) < 2:
        return(list)

    halfIndex = len(list)//2
    firstHalf = list[:halfIndex]
    secondHalf = list[halfIndex:]

    rightSide = mergeSort(firstHalf)
    leftSide = mergeSort(secondHalf)

    mergedList = []
    while len(rightSide) > 0 and len(leftSide) > 0:
        if rightSide[0] < leftSide[0]:
            right = rightSide.pop(0)
            mergedList.append(right)
        else:
            left = leftSide.pop(0)
            mergedList.append(left)

    while len(rightSide) > 0:
        mergedList.append(rightSide.pop(0))

    while len(leftSide) > 0:
        mergedList.append(leftSide.pop(0))

    return(mergedList)

if __name__ == "__main__":
    #aList = [5, 334, 1, 3, 5, 78, 90, 565, 12, 54, 99, 4, 2]
    aList = []
    for i in range(999):
        aList.append(randint(0,5000))

    print(aList)
    print("-\n\n\n")
    print(mergeSort(aList))