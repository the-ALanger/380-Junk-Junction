import tkinter as tk

def delete_item():
    print("Delete Item selected")

def edit_item():
    print("Edit Item selected")

page = tk.Tk()
page.title("Dropdown Example")
page.geometry("300x200")

# --- Create the Menu ---
options_menu = tk.Menu(page, tearoff=0)
options_menu.add_command(label="Delete Item", command=delete_item)
options_menu.add_command(label="Edit Item", command=edit_item)

# --- Create the Options Button ---
def open_menu(event):
    # Popup the menu at the cursor position
    options_menu.tk_popup(event.x_root, event.y_root)

options_button = tk.Button(page, text="Options")
options_button.pack(pady=20)

# Bind left-click to open the menu
options_button.bind("<Button-1>", open_menu)

page.mainloop()
