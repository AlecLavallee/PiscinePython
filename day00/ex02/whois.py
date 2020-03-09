import sys

arg = 0
type1 = "default"
if len(sys.argv) > 2:
	print("ERROR")
else :

	if sys.argv[1].isdigit() :
		arg = int(sys.argv[1])
		if (arg == 0) :
			print("I'm Zero.")
		elif (arg % 2) :
			print("I'm Odd.")
		else :
			print("I'm Even.")
	else :
		print("ERROR")
