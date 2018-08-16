import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) > 0:
		check= input("Did you mean %s instead print yes or no " % get_close_matches(word,data.keys())[0])
		check = check.lower()
		if (check == "yes"  or check == "y"):
			return data[get_close_matches(word,data.keys())[0]]
		else:
			return "Sorry Please check for typo error"
	else:
		return "Sorry No word found in the dictonary" 


word = input("Enter your Word : -  ")
output=translate(word)
if type(output) == list:
	for value in output:
		print(value)
else:
	print(output)
	




