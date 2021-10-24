__author__ = 'mayelespino'
import heapq
from random import randint
#from heapq_showtree import show_tree

heap = []

for i in xrange(0,100):
    item = randint(1,100)
    heapq.heappush(heap, item)
    print item,

print "\n---\n"
# pop them off, in order
while heap:
    print heapq.heappop(heap),

