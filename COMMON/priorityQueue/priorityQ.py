#
#
# From:https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while not q.empty():
    print (q.get())

q.put(10)
q.put(1)
q.put(5)
print(q.get())
print(q.getleft())
#
#
q = Q.PriorityQueue()
q.put((10,'ten'))
q.put((1,'one'))
q.put((5,'five'))
while not q.empty():
    print (q.get())


#
# References
# - https://docs.python.org/3/library/queue.html
# - https://likegeeks.com/python-priority-queue/
