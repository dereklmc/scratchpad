#!/usr/bin/env python

import random

sequences = [ \
	range(10), \
	range(0,20,2), \
	[2,2,2,2,2,2,2,2,2,2,], \
	[3,7,19,26,27,43,323,747,795,1123], \
#	[5,5,5,4,4,4,3,3,3,2] \
]

def binary_search(seq,value):
	#Bounds for subsequence being searched
	first = 0
	last = len(seq)-1
	#Value is not in sequence when bounds cross
	while first <= last:
		#Middle is halfway between bounds.
		middle = (last + first)/2
		probe = seq[middle]
		#Middle separates subsequence into two parts:
		#If value in first part, then look at new subsequence
		#If value is the middle, then return index of middle
		#Otherwise, search the second part.
		if probe < value:
			first = middle + 1
		elif value is probe:
			return middle, probe
		else: #if value  probe:
			last = middle - 1
	#Can't find value!
	return -1, None

for seq in sequences:
	search_for = random.choice(seq)
	print "Searching for [ %s ] in range:   %s" % (search_for, seq)
	index, value = binary_search(seq, search_for)
	print "Found [ %s ] at index: [ %s ]" % (value, index)
