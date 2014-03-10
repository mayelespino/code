#!/usr/bin/env python

class LogArgumentsDecorator(object):
        def __init__(self, orig_func):
                self.orig_func = orig_func
                print 'started logging: %s' % orig_func.__name__

        def __call__(self,  *args, **kwargs):
                print 'args: %s' % args
                print 'kwargs:%s'% kwargs
                return self.orig_func(*args, **kwargs)

@LogArgumentsDecorator      
def sum_of_squares(a, b):
        return a*a + b*b

print sum_of_squares(3, b=4)