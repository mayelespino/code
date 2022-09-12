import heapq
from numpy.random import seed
from numpy.random import randint
# seed random number generator
seed(1)
# generate some integers

def NLargestWithHeap(inList, n):
    result = sorted(list(heapq.nlargest(n,inList)))
    return(result[0])

def NLargestWithSet(inList, n):
    uniqueList = list(set(inList))
    sortedList = sorted(uniqueList, reverse = True)
    return(sortedList[n-1])

def NLargestWithQueue(inList, n):
    nQueue = [0] * n
    top = n - 1
    bottom = 0

    for num in inList:
        if num > nQueue[bottom]:
            nQueue.append(num)
            nQueue.pop(0)
            sorted(nQueue)

    return nQueue[bottom]

largeList = [i for i in range(20,11500)] 
smallRandomList = randint(0, 10, 20)
largeRandomList = randint(0, 1000000, 1000000)

print("\nWith Heap")
print(NLargestWithHeap([1,2,3,4,5,6,7,8,9,0],3))
print(NLargestWithHeap(largeList,3))
print(NLargestWithHeap(smallRandomList,2))
print(NLargestWithHeap(largeRandomList,99))

print("\nWith Set, this is a bad solution")
print(NLargestWithSet([1,2,3,4,5,6,7,8,9,0],3))
print(NLargestWithSet(largeList,3))
print(NLargestWithSet(smallRandomList,2))
print(NLargestWithSet(largeRandomList,99))

print("\nWith Queue")
print(NLargestWithQueue([1,2,3,4,5,6,7,8,9,0],3))
print(NLargestWithQueue(largeList,3))
print(NLargestWithQueue(smallRandomList,2))
print(NLargestWithQueue(largeRandomList,99))

# References
# - https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# - https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
