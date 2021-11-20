from random import randint
from threading import Thread


# class ThreadWithReturnValue(Thread):
#     def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
#         Thread.__init__(self, group, target, name, args, kwargs, Verbose)
#         self._return = None
#     def run(self):
#         if self._Thread__target is not None:
#             self._return = self._Thread__target(*self._Thread__args,
#                                                 **self._Thread__kwargs)
#     def join(self):
#         Thread.join(self)
#         return self._return


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return
# Exceptions

def mergeSort(list):    
    if len(list) < 2:
        return(list)

    halfIndex = len(list)//2
    firstHalf = list[:halfIndex]
    secondHalf = list[halfIndex:]

    T1 = ThreadWithReturnValue(target=mergeSort, args=(firstHalf,))
    T1.start()
    
    T2 = ThreadWithReturnValue(target=mergeSort, args=(secondHalf,))
    T2.start()
    rightSide = T1.join()
    leftSide = T2.join()

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

#
# Links:
# https://stackoverflow.com/questions/11968689/python-multithreading-wait-till-all-threads-finished
# https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
# https://stackoverflow.com/questions/15349997/assertionerror-when-threading-in-python
# https://newbedev.com/how-to-get-the-return-value-from-a-thread-in-python
#