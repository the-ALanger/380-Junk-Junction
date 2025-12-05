import tkinter as tk
from tkinter import ttk, messagebox
from UserCurrent import UserCurrent
from InventoryDatabase import InventoryDatabase
from ImagePopup import ImagePopup

class UserPage(tk.Frame):
    '''
    UserPage    
    11/18/25
    Sarkis Nazaryan
    
    UserPage class is responsible for displaying the items and user information
    posted by the currently logged-in user. 
    '''
    
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
        
        # Create title
        title = tk.Label(self, text=f"Your Items", bg="#791919", fg="white",
                         font=("Times New Roman", 20), anchor="center")
        title.pack(fill="x", side="top")

        left_banner = tk.Frame(self, width=50, bg="#312b2b")
        left_banner.pack(side="left", fill="y")

        right_banner = tk.Frame(self, width=50, bg="#312b2b")
        right_banner.pack(side="right", fill="y")
        
        # Create scrollable area
        scroll_container = tk.Frame(self, bg="#2a6cc8")
        scroll_container.pack(fill="both", expand=True)

        canvas = tk.Canvas(scroll_container, bg="#205fb7", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        center_area = tk.Frame(canvas, bg="#fafafb")
        canvas_window = canvas.create_window((0, 0), window=center_area, anchor="nw")
        
        for i in range(2):
            center_area.columnconfigure(i, weight=1, uniform="col")
            center_area.rowconfigure(i, weight=1, uniform="row")
            
        items = InventoryDatabase.get_items_with_user_id(user_id)

        if items:
            for i, item in enumerate(items):
                self.User_post(center_area, item.itemImage, 
                              f"{item.itemName} - ${item.itemPrice}",
                              item.itemDescription, row=i//2, col=i%2)
        else:
            no_items_label = tk.Label(center_area, text="No items found.", font=("Times New Roman", 12))
            no_items_label.grid(row=0, column=0, pady=20)
        
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_window, width=canvas.winfo_width())

        center_area.bind("<Configure>", update_scroll_region)
        canvas.bind("<Configure>", update_scroll_region)
        
        # Navigation buttons
        tk.Button(self, text='Log Out', width=15,
                  command=lambda: self.controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='Home Page', width=15,
                  command=lambda: self.controller.show_frame("HomePage")).pack(side="bottom", pady=5)

    def on_item_click(self, item):
        messagebox.showinfo("Item", f"You clicked: {item.itemName}")

    def User_post(self, parent, image_path, caption, description, row, col):   
        frame = ttk.Frame(parent, padding=10)
        frame.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        frame.columnconfigure(0, weight=1)

        try:
            photo = tk.PhotoImage(file=image_path)
            # Resize image by subsampling (scale down by factor of 2 if too large)
            if photo.width() > 200 or photo.height() > 150:
                scale_x = max(1, photo.width() // 200)
                scale_y = max(1, photo.height() // 150)
                scale = max(scale_x, scale_y)
                photo = photo.subsample(scale, scale)
        except tk.TclError as e:
            print(f"Image load error for '{image_path}': {e}")
            # Create a gray placeholder with text
            photo = tk.PhotoImage(width=200, height=150)
            photo.put("gray", to=(0, 0, 200, 150))

        img_label = ttk.Label(frame, image=photo)
        img_label.image = photo  # keep reference
        img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

        img_label.bind("<Button>", lambda e, p = image_path, c = caption, d = description : ImagePopup(self, p, c, d))

        text_label = ttk.Label(frame, text=caption, font=("Times New Roman",10), wraplength=200)
        text_label.grid(row=1, column=0, sticky="s")