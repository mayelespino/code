#!/usr/bin/python
"""
Implement a stack data structure using two queues.

Author: Mayel Espino
"""

import Queue
import random

class MyStack():
    tempQueue = None
    queueA = Queue.Queue()
    queueB = Queue.Queue()

    def push(self, inValue):
        try:
            self.queueB.put(inValue)
            while not self.queueA.empty():
                self.queueB.put(self.queueA.get())
            self.tempQueue = self.queueA
            self.queueA = self.queueB
            self.queueB = self.tempQueue
        except asyncio.QueueFull:
            print "Queue is full."
            return False
        return True

    def pop(self):
        return (self.queueA.get())

    def isEmpty(self):
        try:
            return(self.queueA.empty())
        except asyncio.QueueEmpty:
            print "Queue is empty"
        return None


if __name__ == '__main__':

    aStack = MyStack()

    for aNumber in xrange(100):
        aStack.push(aNumber)

    while not aStack.isEmpty():
        print aStack.pop()