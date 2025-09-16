
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
tk.geometry("600x600")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)
label = tkinter.Label(frame, text="Hello, World")
label2 = tkinter.Label(frame, text="Sarkis was here")
label.pack(fill=X, expand=1)
label2.pack(fill=X, expand=1)
button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=RIGHT)
tk.mainloop()