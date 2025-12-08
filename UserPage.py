import tkinter as tk
from tkinter import ttk, messagebox
from UserCurrent import UserCurrent
from InventoryDatabase import InventoryDatabase
from UserImagePopup import UserImagePopup
from HomePage import HomePage

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
                              item.itemDescription, row=i//2, col=i%2, item=item)
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
        # replaced: show AddItemPage -> now prompts for item details inline
        tk.Button(self, text='Add New Item', width=15,
                  command=self.prompt_new_item).pack(side="bottom", pady=5)
    
    # def on_item_click(self, item):
    #     messagebox.showinfo("Item", f"You clicked: {item.itemName}")

    def User_post(self, parent, image_path, caption, description, row, col, item=None):   
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

        img_label.bind("<Button>", lambda e, p=image_path, c=caption, d=description, it=item: UserImagePopup(self, p, c, d, item=it))

        text_label = ttk.Label(frame, text=caption, font=("Times New Roman",10), wraplength=200)
        text_label.grid(row=1, column=0, sticky="s")

    def prompt_new_item(self):
        """Open a dialog to collect new item details and add to InventoryDatabase."""
        user_id = UserCurrent.get_current_user_id()
        if not user_id:
            messagebox.showwarning("Error", "No user logged in.")
            self.controller.show_frame("SignInPage")
            return

        dlg = tk.Toplevel(self)
        dlg.title("Add New Item")
        dlg.grab_set()

        ttk.Label(dlg, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        name_var = tk.StringVar()
        ttk.Entry(dlg, textvariable=name_var, width=40).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(dlg, text="Price:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        price_var = tk.StringVar()
        ttk.Entry(dlg, textvariable=price_var, width=20).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(dlg, text="Condition:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        cond_var = tk.StringVar()
        cond_combo = ttk.Combobox(dlg, textvariable=cond_var, values=["New", "Like New", "Good", "Fair", "Poor"], state="readonly", width=18)
        cond_combo.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        cond_combo.set("Good")

        # Category input
        ttk.Label(dlg, text="Category:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        cat_var = tk.StringVar()
        cat_combo = ttk.Combobox(dlg, textvariable=cat_var,
                                 values=["Electronics", "Books", "Clothing", "Furniture", "Sports", "Toys", "Other"],
                                 state="readonly", width=18)
        cat_combo.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        cat_combo.set("Other")

        ttk.Label(dlg, text="Description:").grid(row=4, column=0, sticky="ne", padx=5, pady=5)
        desc_text = tk.Text(dlg, width=40, height=6)
        desc_text.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(dlg, text="Image Path (optional):").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        image_var = tk.StringVar()
        ttk.Entry(dlg, textvariable=image_var, width=40).grid(row=5, column=1, padx=5, pady=5)

        def on_save():
            name = name_var.get().strip()
            price_s = price_var.get().strip()
            condition = cond_var.get().strip()
            category = cat_var.get().strip()
            description = desc_text.get("1.0", "end").strip()
            image = image_var.get().strip()
            if image == "":
                image = "images/default.png"

            if not name:
                messagebox.showwarning("Validation", "Name is required.")
                return
            try:
                price = float(price_s) if price_s else 0.0
            except ValueError:
                messagebox.showwarning("Validation", "Price must be a number.")
                return

            try:
                InventoryDatabase.create_new_item(name, description, condition, category, price, image)
            except Exception as e:
                messagebox.showerror("Database Error", f"Failed to add item: {e}")
                return
            finally:
                dlg.destroy()
                self.refresh_items()
                # Get the HomePage frame and refresh it
                home_page = self.controller.frames["HomePage"]
                home_page.update_items()

        btn_frame = ttk.Frame(dlg)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)
        ttk.Button(btn_frame, text="Save", command=on_save).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Cancel", command=dlg.destroy).pack(side="left", padx=5)