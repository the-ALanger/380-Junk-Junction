
import tkinter
from tkinter.constants import *
from tkinter import *

homepage = tkinter.Tk()
homepage.geometry("800x600")
frame = tkinter.Frame(homepage, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)

homepage.title('Junk Junction')

title = tkinter.Label(frame, text = 'Junk Junction', bg="darkred", font = ("Times New Roman", 12))
title.pack(fill=X, side=TOP, expand=1)

"""
Label(homepage, text='First Name').grid(row=1)
Label(homepage, text='Last Name').grid(row=1)
e1 = Entry(homepage)
e2 = Entry(homepage)
e1.grid(row=0, column=0)
e2.grid(row=1, column=0)
"""

button = tkinter.Button(frame, text='Return to Desktop', width=15, command=homepage.destroy)
button.pack()
"""
label = tkinter.Label(frame, text="Junk Junction")
label.pack(fill=X, expand=2, side=TOP)

button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=RIGHT)
"""
homepage.mainloop()


"""tk = tkinter.Tk()
tk.geometry("600x600")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
"""