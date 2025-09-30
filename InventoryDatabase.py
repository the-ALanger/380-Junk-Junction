import csv
import tkinter
from tkinter.constants import *
from tkinter import *

tk = tkinter.Tk()
tk.geometry("600x600")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH, expand=1)

csv_content = ""
with open('JJInventoryDatabase - Sheet1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)  # For comma-separated values
        # For tab-separated values, use: reader = csv.reader(file, delimiter='\t')   
    for row in reader:
        csv_content += "\t".join(row) + "\n"
        
text_widget = tkinter.Text(frame, wrap="none")
text_widget.insert(tkinter.END, csv_content)
text_widget.pack(fill=BOTH, expand=1)        
        
button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=RIGHT)
tk.mainloop()
 
 