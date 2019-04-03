# To start the program, please open a terminal/prompt and go to the directory
#that this file and 'data.json' are saved. With python installed, run
#'python app1.py'

import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Type Y for yes or N for no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)
