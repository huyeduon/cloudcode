import sys, os
num_word = 0

def numWord(word, stringOfLine):
    lines = stringOfLine.split()
    for word in lines:
        if word == 'up' or word == 'up,':
            num_word += 1
    return num_word

stringOfLine = 'Tunnel1 is up, line protocol is up'
word = 'up'
numUp = num_word(word,stringOfLine)