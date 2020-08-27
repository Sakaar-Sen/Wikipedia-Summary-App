import wikipedia
import os
from tkinter import *
from tkinter import messagebox



def search():
    try:
        TheAns =wikipedia.summary(thing.get(), 10)
        with open("search_result.txt", "w") as file:
            file.write(TheAns)
    except:
        messagebox.showinfo("Error", "Please try again using different keywords")


def OPEN():
    os.system("search_result.txt")


master = Tk()
master.title("Wikipedia Summary App")

label1 = Label(master, text = "Wikipedia Search", font=("Times New Roman", 30, "bold")).grid(row = 0, column = 0, padx = 10, pady = 5, ipadx = 10, ipady = 20)
label2 = Label(master, text = "Enter something in 2 words or more", font=("Arial", 12)).grid(row = 1, column = 0, padx = 20)
thing = Entry(master)
button1 = Button(master, text = "Search and Save", command = search).grid(row = 3, column = 0, ipadx = 10, ipady =10, pady = 20)
button2 = Button(master, text= "Open", command = OPEN).grid(row =4 , column = 0 , ipadx = 10, ipady =10, padx = 20)

thing.grid(row = 2, column = 0, ipadx = 20, ipady = 10, padx = 10)

master.mainloop()


