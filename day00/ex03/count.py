import sys
import string

def text_analyzer(str) :
		value = len(str)
		upper = 0
		lower = 0
		punc = 0
		spaces = 0
		if value > 0 :
			for i in str :
				if i.isupper() :
					upper += 1
				if i.islower() :
					lower += 1
				if i.isspace() :
					spaces += 1
				for x in string.punctuation :
					if i == x :
						punc += 1
			print("The text contains %d characters" % (upper + lower + spaces + punc))
			print("%d upper letters" % (upper))
			print("%d lower letters" % (lower))
			print("%d punctuation marks" % (punc))
			print("%d spaces" % (spaces))
		else :
			print("Gimme something mate!")

if len(sys.argv) < 3 :
	text_analyzer(sys.argv[1])
else :
	print("WoW too much text!")