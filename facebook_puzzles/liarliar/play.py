
import time

ff = open("tests/5000_5000.in")

tA = time.time()

lines = ff.readlines()

tB = time.time()

filterLines = filter(lambda l: len(l.strip().split()) is 2, lines)

tC = time.time()

print tB - tA

print tC - tB
