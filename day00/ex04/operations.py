import sys

args = len(sys.argv)
if args > 2 and args < 4 :
	if (sys.argv[1].isdigit() and sys.argv[2].isdigit()) :
		first = int(sys.argv[1])
		second = int(sys.argv[2])
		print("first : %d and second : %d" % (first, second))
		print("addition : %d" % (first + second))
		print("soustraction : %d" % (first - second))
		print("multiplication : %d" % (first * second))
		print("divison : %d" % (first / second))
		print("modulo : %d" % (first % second))
	else :
		print("Those 2 are not integers mate!")
else :
	print("I need two integers mate!")
