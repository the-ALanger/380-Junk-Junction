import csv
import tkinter
from tkinter.constants import *
from tkinter import *
from InventoryDatabase import *


tk = tkinter.Tk()
tk.geometry("600x600")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)
        
Inv_Data = InventoryDatabase()
        
text_widget = tkinter.Text(frame, wrap="none")
text_widget.insert(tkinter.END, Inv_Data.csv_w_label)
text_widget.pack(fill=BOTH, expand=1)        
        
button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=RIGHT)
tk.mainloop()
 
 