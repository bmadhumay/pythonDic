import pyttsx3
import speech_recognition as sr
import pyaudio
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
from tkinter import *
from PIL import Image, ImageTk
import json
from difflib import get_close_matches

voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_id)
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with open('data.json','r')as json_file:
    data_load = json.load(json_file)

def search_word(word):
    if word in data_load:
        meaning_word.delete(1.0,END)
        meaning_word.config(fg = "red")
        meaning_word.insert(END, data_load[word])
    elif len(get_close_matches(word, data_load.keys()))>0:
        meaning_word.config(fg = "red")
        meaning_word.delete(1.0,END)
        meaning_word.insert(END,"Were You Finding {} and meaning is : {} ".format(get_close_matches(word, data_load.keys())[0],data_load[get_close_matches(word,data_load.keys())[0]]))
        final = get_close_matches(word, data_load.keys())
    op=meaning_word.get(1.0,END)
    print(op)
    speak(op)
        
    
root = Tk()
root.title("My Own Dictionary")

image = Image.open('dict.jpg')
image_picture = ImageTk.PhotoImage(image)
dest_pic = Label(root, image=image_picture)
dest_pic.pack()

a = StringVar()
word_1 = Entry(root, textvariabl = a, background = "blue", fg = "white", font =  ('arial',40,"bold"))
word_1.place(relx=0.185, rely=0.70, relheight=0.082)

button_1 = Button(root, text="Search The Word...", command = lambda:search_word(a.get()), background = "red", fg = "white", font = ("arial",40,"bold"))
button_1.place(relx=0.25, rely=0.85, relheight=0.052)

meaning_word = Text(root, background = "white", font = ('arial',40,"bold"))
meaning_word.place(relx=0.200, rely=0.05, relheight=0.16, relwidth=0.63)

root.mainloop()
