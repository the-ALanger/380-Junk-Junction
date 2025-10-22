
import tkinter
from tkinter.constants import *
from tkinter import *

UserPage = Tk()
UserPage.geometry("800x600")
frame = Frame(UserPage, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)

#Page Title
UserPage.title('Junk Junction')

#Top Title
title = Label(frame, text = 'Junk Junction', bg="darkred", fg = "white", font = ("Times New Roman", 20), anchor="center")
title.pack(fill=X, side=TOP)

#Left Banner Frame
left_banner = Frame(frame, width=50, bg="#453b3b")
left_banner.pack(side="left", fill="y")

# Right Banner Frame
right_banner = Frame(frame, width=50, bg="#453b3b")
right_banner.pack(side="right", fill="y")

#Exit Button
button = Button(frame, text='Return to Desktop', width=15, command=UserPage.op)
button.pack(side=BOTTOM, padx=10)


UserPage.mainloop()


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
