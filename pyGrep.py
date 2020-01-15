#! /bin/python

def Grep(word, file):
	f = open(file, 'r')
	lines = f.readlines()
	f.close()
	has_word = lambda line: line.find(word) != -1
	output = filter(has_word, lines)
	return "".join(output)

print(Grep('html', 'index.html'))
