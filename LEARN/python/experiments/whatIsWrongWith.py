#!/usr/bin/python

def foo(data=[]):
    data.append(1)
    print len(data)
    
def bar(data=0):
    print data
    
foo()
foo()
foo()
bar()
bar(2)
bar()