import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data [get_close_matches(word, data.keys())[0]]
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter a word: ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)




