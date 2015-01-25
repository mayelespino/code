__author__ = 'mayelespino'
from collections import namedtuple
from operator import itemgetter

Item = namedtuple('Item', 'letter, count')
ItemList = [
    Item('a',1),
    Item('e',12),
    Item('b',15),
    Item('c',3)
            ]
SL1 = sorted(ItemList, key=itemgetter(0))
SL2 = sorted(ItemList, key=itemgetter(1), reverse=True)

for item in ItemList:
    print item[0],item[1]

print '----'
for item in SL1:
    print item
print '----'
for item in SL2:
    print item

print '----'
