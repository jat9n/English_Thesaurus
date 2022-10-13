import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def dict(w):
    w = w.lower()
    if w in data:
        return(data[w])
    elif len(get_close_matches(w, data.keys())) > 0:
        y = input(f"did u mean {get_close_matches(w, data.keys())[0]} instead? enter y if yes n if no")
        if y == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return ("word not found") 
    else:
        return ("word not found")

    
word = input("enter the word: ")
output = dict(word)

if type(output) == list:
    for item in output:
        print(item)
else: print(output)