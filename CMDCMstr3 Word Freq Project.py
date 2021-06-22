#!/usr/bin/python3
# CYB333: Final Course Project
#Project Title: Word Frequency 
#Author: CMDCMstr3
#Date: June 22, 20121


import string
# Opens and reads text file.
text = open("PythonMission.txt", "r") 
# This will create the dictionary that will be used.
d = dict() 
# This creates a loop through PythonMission.txt
for line in text:
# Changes all words in text to lower case.	
	line = line.lower()
# Removes all punctualation. Note: It took me a while to figure this out.	
	line = line.translate(line.maketrans("", "", string.punctuation))
	
	words = line.split(" ")
# starts an iteration through each word.
for word in words:
	
	if word in d:
# Counts each word by one incrementally.		
		d[word] = d[word] + 1
	
	else:
# Those words that appear once is assigned a 1. 	
		d[word] = 1
# Printing format for words in the dictionary.
for key in list(d.keys()):
	
	print(key + ": ", d[key], ', ', sep='', end='')
	
	 

