import tkinter as tk
from tkinter import *
from tkinter.constants import *

## Page Attributes ##
page = tk.Tk()
page.geometry("800x600")
page.title('Junk Junction')


# ------------------ Sign-In Page ------------------ #
UserSignInPage = Frame(page)
UserSignInPage.grid(row=0, column=0, sticky='nsew')

Label(UserSignInPage, text='Email').grid(row=0)
Label(UserSignInPage, text='Password').grid(row=1)

e1 = Entry(UserSignInPage)
e2 = Entry(UserSignInPage, show="*")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


# ------------------ Home Page ------------------ #
HomePage = Frame(page)
HomePage.grid(row=0, column=0, sticky='nsew')

# Top Title
title = Label(HomePage, text = 'Junk Junction', bg="#791919", fg = "white", 
             font = ("Times New Roman", 20), anchor="center")
title.pack(fill=X, side=TOP)

# Left Banner
left_banner = Frame(HomePage, width=50, bg="#312b2b")
left_banner.pack(side="left", fill="y")

# Right Banner
right_banner = Frame(HomePage, width=50, bg="#312b2b")
right_banner.pack(side="right", fill="y")

# Exit Button (return to sign-in)
Exit_Button = Button(HomePage, text='Return to Sign In', width=15,
                     command=lambda: UserSignInPage.tkraise())
Exit_Button.pack(side=BOTTOM, pady=10)

# ------------------ Buttons on Sign-In ------------------ #
SignIn_Button = Button(UserSignInPage, text='Sign In', width=10,
                       command=lambda: HomePage.tkraise())
SignIn_Button.grid(row=2, column=1, pady=10)

ExitApp_Button = Button(UserSignInPage, text='Exit App', width=10,
                        command=page.destroy)
ExitApp_Button.grid(row=3, column=1, pady=10)

# ------------------ Initialize ------------------ #
UserSignInPage.tkraise()  # Show sign-in page first

page.mainloop()