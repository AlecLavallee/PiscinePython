import sys

array = []
for arg in sys.argv[1:]:
	array.append((arg[::-1]).swapcase())
array.reverse()
for x in range(len(array)) :
	print(array[x])
