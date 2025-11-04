import csv
import tkinter
from tkinter.constants import *
from tkinter import *
from InventoryDatabase import InventoryDatabase
from ItemImages import item_image_paths

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
 
################################################ Side-by-Side Display ##############################################
# root = tk.Tk()
# root.title("Side-by-Side Image Display")

# # Create a frame to hold the images horizontally
# frame = tk.Frame(root)
# frame.pack()

# # Load and display each image side-by-side
# photos = []
# for path in item_image_paths(item_ID=1001):
#     photo = tk.PhotoImage(file=path)
#     photos.append(photo)
#     label = tk.Label(frame, image=photo)
#     label.pack(side=tk.LEFT, padx=5)

# root.mainloop()