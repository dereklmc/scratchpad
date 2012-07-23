#!/usr/bin/env python

'''
Approximates a y for a value of t given a function, f, of y and t.
Uses Euler's method.

Written, partly, in collaboration with Erin McLean
'''

import math
from decimal import * 
# Integer and Floating Point math results in eroneous decimals. 
# Use this module to fix that.

getcontext().prec = 6

def iterateY(f, h):
    def nextY(t,y):
        return y + h*f(t,y)
    return nextY

'''
Get a decimal range to iterate over.
Goes from start to stop-1 in increments 
'''
def frange(start,stop,step=1.0):
    current = start
    while current < stop:
        yield current
        current += step        

def eulersMethod(nextY, y0, theRange):
    y = y0
    for t in theRange:
        y = nextY(t, y)
    return y

def evalFunction(f, y0, endVals):
    for step in [0.1,0.05,0.025,.01]:
        step = Decimal(str(step))
        nextY = iterateY(f, step)
        for end in endVals:
            end = Decimal(str(end))
            r = frange(Decimal('0'),end,step)
            e = eulersMethod(nextY, 0, r)
            yield (step,end,e)

endValsStandard = [0.1,0.2,0.3,0.4]

funcArgs = {
    "1.": ( \
        lambda t,y: Decimal('3.0')+t-y, \
        1, \
        endValsStandard \
    ), \
    "2.": ( \
        lambda t,y: Decimal('2.0')*y - Decimal('1.0'), \
        1, \
        endValsStandard \
    ), \
    "4.": ( \
        lambda t,y: Decimal('3.0')*Decimal(str(math.cos(t))) - Decimal('2.0')*y, \
        0, \
        endValsStandard \
    ), \
    "11.": ( \
        lambda t,y: Decimal('5.0') - Decimal('3.0')*Decimal(str(math.sqrt(y))), \
        2, 
        [0.5,1.0,1.5,2.0,2.5,3.0] \
    ), \
    "16.": ( \
        lambda t,y: t*t + y*y, \
        1, \
        [0.2,0.4,0.6,0.8,1.0] \
    ) \
}

try:
    for name in funcArgs.iterkeys():
        print "\n----------------------------------------------\
        \n%s\n----------------------------------------------" % name
        f, y0, endVals = funcArgs[name]
        for result in evalFunction(f, y0, endVals):
            print "%s\t%s\t:\t%s" % result
except TypeError, e:
    print e
