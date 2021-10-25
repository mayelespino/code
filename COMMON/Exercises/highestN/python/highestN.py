import heapq
from numpy.random import seed
from numpy.random import randint
# seed random number generator
seed(1)
# generate some integers

def NLargest(inList, n):
    result = sorted(list(heapq.nlargest(n,inList)))
    return(result[0])

def NLargestWithSet(inList, n):
    uniqueList = list(set(inList))
    sortedList = sorted(uniqueList, reverse = True)
    return(sortedList[n])


print(NLargest([1,2,3,4,5,6,7,8,9,0],3))
print(NLargest([i for i in range(20,11500)],3))
print(NLargest(randint(0, 10, 20),2))
print(NLargest(randint(0, 1000000, 1000000),99))

print(NLargestWithSet([1,2,3,4,5,6,7,8,9,0],3))
print(NLargestWithSet([i for i in range(20,11500)],3))
print(NLargestWithSet(randint(0, 10, 20),2))
print(NLargestWithSet(randint(0, 1000000, 1000000),99))



# References
# - https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# - https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
