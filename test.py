import sys, os

def countKeyWord(key_word, key_string):
	num_word = 0
	up = key_string.replace(',', ' ')
	strlist = list(up.split(" "))
	for word in strlist:
		if word==key_word: 
			num_word += 1

	print ("Number of " + key_word + " in " + key_string + " is " + str(num_word))

def main():
	key_word = "up"
	key_string = 'Tunnel1 is up, line protocol is up'
	countKeyWord(key_word, key_string)

if __name__ == '__main__':
    main()