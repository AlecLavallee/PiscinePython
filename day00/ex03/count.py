import sys
import string

def text_analyzer(text = None) :
	""" This function counts the number of upper characters, lower characters, punctuation and spaces in a given text. """
	if not text:
		text = input("What is the text to analyze? \n>> ")
	value = len(text)
	upper = 0
	lower = 0
	punc = 0
	spaces = 0
	if value > 0 :
		for i in text :
			if i.isupper() :
				upper += 1
			if i.islower() :
				lower += 1
			if i.isspace() :
				spaces += 1
			if i in string.punctuation :
				punc += 1
		print("The text contains %d characters" % (upper + lower + spaces + punc))
		print("%d upper letters" % (upper))
		print("%d lower letters" % (lower))
		print("%d punctuation marks" % (punc))
		print("%d spaces" % (spaces))
	else :
		print("String is empty")