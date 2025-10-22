from tkinter import *

UserPage = Tk()
UserPage.geometry("800x600")
frame = Frame(UserPage, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)

#Page Title
UserPage.title('Junk Junction')

title = Label(frame, text = 'Junk Junction', bg="darkred", fg = 'white', font = ("Times New Roman", 20), anchor="center")
title.pack(fill=X, side=TOP)

#Left Banner Frame
left_banner = Frame(frame, width=50, bg="#453b3b")
left_banner.pack(side="left", fill="y")

# Right Banner Frame
right_banner = Frame(frame, width=50, bg="#453b3b")
right_banner.pack(side="right", fill="y")

button = Button(frame, text='Return to Desktop', width=15, command=UserPage.destroy)
button.pack(side=BOTTOM, padx=10)


UserPage.mainloop()