import tkinter as tk
from tkinter import messagebox
from UserCurrent import UserCurrent
from InventoryDatabase import InventoryDatabase

class UserPage(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.items_frame = None
        
    def refresh_items(self):
        """Refresh the page when user logs in."""
        for widget in self.winfo_children():
            widget.destroy()
        
        user_id = UserCurrent.get_current_user_id()
        
        if not user_id:
            messagebox.showwarning("Error", "No user logged in.")
            self.controller.show_frame("SignInPage")
            return
            
        items = InventoryDatabase.get_items_with_user_id(user_id)

        title = tk.Label(self, text=f"Your Items", font=("Times New Roman", 14))
        title.pack(pady=10)
        
        if items:
            for item in items:
                btn = tk.Button(self, text=item.itemName,
                               command=lambda i=item: self.on_item_click(i))
                btn.pack(pady=5)
        else:
            tk.Label(self, text="No items found.").pack(pady=10)
        
        tk.Button(self, text='Log Out', width=15,
                  command=lambda: self.controller.show_frame("SignInPage")).pack(side="bottom", pady=10)

    def on_item_click(self, item):
        messagebox.showinfo("Item", f"You clicked: {item.itemName}")