import tkinter as tk  
from tkinter import ttk
  
win = tk.Tk()# Application Name  
win.title("Python GUI App")# Label  
lbl = ttk.Label(win, text = "Enter the name:").grid(column = 0, row = 0)# Click event  
def click():   
    print("Hi," + name.get())# Textbox widget  
name = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 12, textvariable = name).grid(column = 0, row = 1)# Button widget  
button = ttk.Button(win, text = "submit", command = click).grid(column = 1, row = 1)  
win.mainloop()
