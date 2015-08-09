#!/usr/bin/python

import threading
import time
import sys

#exitFlag = 0

class elevatorClass (threading.Thread):
    def __init__(self, elevatorID, name, initialFloor):
        threading.Thread.__init__(self)
        self.threadID = elevatorID
        self.name = name
        self.current_floor = initialFloor
        self.requested_floor = initialFloor
        self.new_floor = initialFloor
        self.stopIT = False
    def wait(self):
        time.sleep(2)
    def run(self):
        while not self.stopIT:
            sys.stdout.write("[%s] %d -> %d\n" % (self.name, self.current_floor, self.requested_floor))
            if self.current_floor < self.requested_floor:
                self.current_floor += 1
            elif self.current_floor > self.requested_floor:
                self.current_floor -= 1
            elif self.current_floor == self.current_floor and self.requested_floor != self.new_floor:
                self.requested_floor = self.new_floor
            self.wait()
    def requestFloor(self,newFloor):
        sys.stdout.write("%s - new floor request: %d\n" % (self.name, newFloor))
        self.new_floor = newFloor
    def stopElevator(self):
        sys.stdout.write("%s -  stop requested.\n" % self.name)
        self.stopIT = True


# Create new threads
elevator1 = elevatorClass(1, "Elevator-1", 1)
elevator2 = elevatorClass(2, "Elevator-2", 2)
elevator3 = elevatorClass(3, "Elevator-3", 25)

# Start new Threads
elevator1.start()
elevator2.start()
elevator3.start()
#
elevator1.requestFloor(10)
elevator2.requestFloor(8)
time.sleep(5)
elevator3.requestFloor(1)
#
time.sleep(30)
elevator1.requestFloor(2)
elevator2.requestFloor(1)
time.sleep(30)
print "Stopping Elevators 1 and 2."
elevator1.stopElevator()
elevator2.stopElevator()
#
time.sleep(10)
print "Stopping Elevator 3."
elevator3.stopElevator()


print "Exiting Main Thread"