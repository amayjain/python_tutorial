import json
from difflib import get_close_matches # get_close_matches(value, possibilities, n = 3, cutoff = 0.6) --> compares strings
                                      # value compared to possibilities; "n" is number of possibilities returned; cutoff is ratio of how similar a value is to a possibility
                                      # returns a list with selected possibilities

data = json.load(open("data.json")) #converts json to a python dictionary with values and keys
                                    #json values are a list of definitions

# print(type(data))

# print(data["rain"])

def translate(w):
    w = w.lower()
    if w in data:
        return data[w] 
    elif len(get_close_matches(w, data.keys())) > 0: #makes sure possibilities list isn't empty
        yn = input("Did you mean {}? Enter Y if yes, or N if no: ".format(get_close_matches(w, data.keys())[0])) #accessing first element of possibilities list
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ") #program starts execution with this

output = (translate(word)) #either generates a list or string

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

