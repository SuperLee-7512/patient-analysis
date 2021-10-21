"""
This module counts counts the number of line in standard

"""

import sys

count = 0
for line in sys.stdin:
	count +=1

print(count, "lines in standard input")
