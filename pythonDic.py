from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches 

with open('data.json', 'r') as json_file:
    data_load = json.load(json_file)

def search_word(word):
    if word in data_load:
        meaning_word.delete(1.0,END)
        meaning_word.config(fg = "red")
        meaning_word.insert(END,data_load[word])
    elif len(get_close_matches(word, data_load.keys()))>0:
        meaning_word.config(fg = "red")
        meaning_word.delete(1.0,END)
        meaning_word.insert(END,"Were You Finding{} and meaning is : {} ".format(get_close_matches(word, data_load.keys())[0,data_load[get_close_matches(word,data_load.keys())[0]]]))
        final = get_close_matches()

root = Tk()
root.title("My Own Dictionary")

image = Image.open('dict.jpg')
image_picture = ImageTk.PhotoImage(image)
dest_pic = Label(root, image=image_picture)
dest_pic.pack()

a = StringVar()
word_1 = Entry(root, textvariabl = a, background = "blue", fg = "white", font =  ('arial',40,"bold"))
word_1.place(relx=0.185, rely=0.70, relheight=0.082)

button_1 = Button(root, text="Search The Word...", command = lambda:search_word(a.get()), background = "red", fg = "white", font = ('arial',40,"bold"))
button_1.place(relx=0.25, rely=0.85, relheight=0.052)

meaning_word = Text(root, background = "white", font = ('arial',40,"bold"))
meaning_word.place(relx=0.200, rely=0.05, relwidth=0.63, relheight=0.16)


root.mainloop()
