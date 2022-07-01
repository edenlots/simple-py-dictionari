import json
from difflib import get_close_matches
data = json.load(open("data.json"))
#sortedkey=dict(sorted(data.items(), key=lambda item:item[0])) #optional sorting using lambda ;)

def getdata():
    text = input("Word Meaning: ")
    if text in data:
        print(data[text])
    elif text.upper() in data:
        print(data[text.upper()])
    elif text.title() in data:
        print(data[text.title()])
    elif text not in data:
        newtext=get_close_matches(text,data,cutoff=0.6)
        print("Are these the words you're looking for? "+ str(newtext))
        getdata()
    else:
        print("The word does not exist.")
    return ask()
def ask():
    key=input("\nType y to continue or n to exit (and press Enter)-- ")
    if key == "y":
        return getdata()
    elif key == "n":
        quit()
    else:
        print("\nPlease select Y or N")
        return ask()
getdata()
