import json
import tkinter as tk
from tkinter import messagebox
from difflib import get_close_matches

data = json.load(open("data.json"))
# optional sorting using lambda
#sortedkey=dict(sorted(data.items(), key=lambda item:item[0]))

def getdata():
    word = entry.get()

    # When word is found in the dictionary:
    if word in data:
        result_label.config(text=data[word])
    elif word.upper() in data:
        result_label.config(text=data[word.upper()])
    elif word.title() in data:
        result_label.config(text=data[word.title()])

    # When word is not found in the dictionary:
    elif word not in data:
        newtext=get_close_matches(word,data,cutoff=0.4)
        result_label.config(text="Not found. Are these the words you're looking for? "+ str(newtext))
    else:
        messagebox.showinfo("The word does not exist.")


# GUI Setup
root = tk.Tk()
root.title("Simple Py Dictionari")
root.geometry("600x400")
root.resizable(False, False)

# UI Components
tk.Label(root, text="Enter a word:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Search", command=getdata, font=("Arial", 12)).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, fg="blue")
result_label.pack(pady=10)

# Run GUI
root.mainloop()