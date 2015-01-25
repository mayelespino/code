__author__ = 'mayelespino'
from operator import itemgetter

D = {}
DL = []

# why did this not work?
# D['item'] = 'a'
# D['count'] = 1
# DL.append(D)
#
# D['item'] = 'z'
# D['count'] = 1
# DL.append(D)
#
# D['item'] = 'v'
# D['count'] = 10
# DL.append(D)
#
# D['item'] = 'c'
# D['count'] = 15
# DL.append(D)

DL.append({'item':'a','count':10})
DL.append({'item':'z','count':5})
DL.append({'item':'c','count':3})
DL.append({'item':'y','count':20})



SL1 = []
SL2 = []

SL1 = sorted(DL, key=itemgetter('item'))
for l in SL1:
    print l['item'],l['count']

print "----"
SL2 = sorted(DL, key=itemgetter('count'))
for l in SL2:
    print l['item'],l['count']
