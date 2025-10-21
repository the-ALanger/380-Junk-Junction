
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

# Sign In Screen
# Remove three quoatations from top and bottom and run

"""
from tkinter import *

UserSignInPage = Tk()
UserSignInPage.geometry("200x100")

UserSignInPage.title('Sign In')


Label(UserSignInPage, text='Email').grid(row=0)
Label(UserSignInPage, text='Password').grid(row=1)

e1 = Entry(UserSignInPage)
e2 = Entry(UserSignInPage)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#Sign In Button
button = Button(UserSignInPage, text='Sign In', width=10, command=UserSignInPage.destroy)
button.grid(row=2, column=1)


#Exit App Button
button = Button(UserSignInPage, text='Exit App', width=10, command=UserSignInPage.destroy)
button.grid(row=4, column=1)

mainloop()
"""
