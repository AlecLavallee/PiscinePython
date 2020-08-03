import sys

def filter(text = None, n = 0) :
	listofthings = []
	if (listofthings == []) :
		print("this list is empty.")
	res = [listofthings[i] for i in range(len(listofthings)) if len(listofthings[i]) > n]
	print(res)

#if (len(sys.argv) == 2) :
#	if isinstance(sys.argv[2], str) :
#		filter(str(sys.argv[2])