from difflib import get_close_matches
import json

data =  json.load(open("data.json"))
keys = data.keys()

def translate(word):
	if word in data:
		return data[word]
	elif len(get_close_matches(word, keys)) > 0:
		best = get_close_matches(word, keys)[0]
		repsonse = input("Did you mean %s instead? Enter Y if yes, N if no." % best)
		if repsonse == "Y":
			if best in data:
				return data[best]
		elif repsonse == "N":
			return "The word doesn't exist. Try Again."
		else:
			return "Sorry we did not understand your query."
	else:
		return "The word doesn't exist in this dictionary."

word = input("Enter words: ").lower()
output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)