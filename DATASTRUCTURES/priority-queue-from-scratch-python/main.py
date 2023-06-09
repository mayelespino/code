import random
import array

def generateArray(size):
    return random.sample(range(0, 999), size)

class priorityQueue():
    priorityQueue = []
    max_size = 0
    def __init__(self, size):
        self.max_size = size + 1

    def addArray(self, array):
        for i, number in enumerate(array):
            self.add(number)

    def add(self,number):
        size = len(self.priorityQueue)
        if size == 0:
            self.priorityQueue.append(number)
        index = 0
        while index < size:
            if self.priorityQueue[index] < number:
                break
            index += 1
        self.priorityQueue.insert(index, number)

        if len(self.priorityQueue) >= self.max_size:
            del self.priorityQueue[-1]

    def returnQueue(self):
        return self.priorityQueue


if __name__ == '__main__':
    myPQ = priorityQueue(5)
    myArray = generateArray(300)
    print(myArray)
    myPQ.addArray(myArray)
    print(myPQ.returnQueue())

#
# This is a naive implementation of a priority queue, a better implementation is using a minHeap or a maxHeap.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# https://www.tutorialspoint.com/generating-random-number-list-in-python
