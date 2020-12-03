import sys, os

def countKeyWord(key_word, key_string):
	num_word = 0
	up = key_string.replace(',', ' ')
	strlist = list(up.split(" "))
	for word in strlist:
		if word==key_word: 
			num_word += 1
	return num_word
