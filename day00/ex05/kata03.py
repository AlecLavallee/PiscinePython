phrase = "The right format"
length = len(phrase)
string = ''
while length < 42 :
	string += string.join('-')
	length += 1
print(string+phrase[:-1])