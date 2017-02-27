from random import randint

listOfRandomInts = []
for x in xrange(1,10):
    listOfRandomInts.append(randint(0,99))


def mergeSort(listToSort):
    if len(listToSort) <= 1:
        return listToSort

    halfPoint = len(listToSort) / 2
    left = mergeSort(listToSort[:halfPoint])
    right = mergeSort(listToSort[halfPoint:])

    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if len(left) > 0:
        result.extend(mergeSort(left))
    else:
        result.extend(mergeSort(right))

    return result



print listOfRandomInts
sortedList = mergeSort(listOfRandomInts)
print sortedList