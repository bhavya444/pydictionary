import json
from difflib import get_close_matches

data = json.load(open("db.json"))

def translate(w):
    w = w.lower()
 

    if w in data:
        print("")
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        ans = input("Did you mean %s instead? Enter Y|y if yes or N|n if no: " % get_close_matches(w, data.keys())[0])
        if ans == "Y":
            print("")
            return data[get_close_matches(w, data.keys())[0]]
        elif ans == "y":
            print("")
            return data[get_close_matches(w, data.keys())[0]]
        elif ans == "N":
            print("")
            return "Type again"
        elif ans == "n":
            print("")
            return "Type again"
        else:
            print("")
            return "WRONG ENTRY"
    else:
        print("")
        return "The term does not exist."
       
t=True
while t:
 print("")
 print("press ctrl-z to exit")
 print("")
 term = input("enter the word you want to search: ")

 output = translate(term)
 if type(output) == list:
    for item in output:
        print(item)
 else:
   print(output)

