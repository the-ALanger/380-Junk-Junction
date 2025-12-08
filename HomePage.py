import tkinter as tk
from tkinter import ttk, messagebox  
from InventoryDatabase import InventoryDatabase
from UserDatabase import UserDatabase
from HomeImagePopup import HomeImagePopup

class HomePage(tk.Frame):
    '''
    HomePage
    11/18/25
    Sarkis Nazaryan, Leonel Villanueva

    Homepage class is responsible for displaying the main interface of the application, 
    it includes the title, side banners, navigation buttons, and a scrollable area
    that displays user posts with images and captions.
    '''

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text='Junk Junction', bg="#791919", fg="white",
                         font=("Times New Roman", 20), anchor="center")
        title.pack(fill="x", side="top")

        left_banner = tk.Frame(self, width=50, bg="#312b2b")
        left_banner.pack(side="left", fill="y")

        right_banner = tk.Frame(self, width=50, bg="#312b2b")
        right_banner.pack(side="right", fill="y") 
        
        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='User Page', width=15,
                  command=lambda: controller.show_frame("UserPage")).pack(side="bottom", pady=5)
        
        # Category filter frame
        filter_frame = tk.Frame(self, bg="#791919")
        filter_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(filter_frame, text="Filter by Category:").pack(side="left", padx=5)
        
        self.category_var = tk.StringVar(value="All")
        category_combo = ttk.Combobox(filter_frame, textvariable=self.category_var,
                                      values=["All", "Electronics", "Books", "Clothing", "Furniture", "Sports", "Toys", "Other"],
                                      state="readonly", width=15)
        category_combo.pack(side="left", padx=5)
        category_combo.bind("<<ComboboxSelected>>", lambda e: self.update_items())

        ttk.Label(filter_frame, text="Filter by Condition:").pack(side="left", padx=10)
        self.condition_var = tk.StringVar(value="All")
        condition_combo = ttk.Combobox(filter_frame, textvariable=self.condition_var,
                           values=["All", "Like New", "Good", "Fair", "Poor"],
                           state="readonly", width=12)
        condition_combo.pack(side="left", padx=5)
        condition_combo.bind("<<ComboboxSelected>>", lambda e: self.update_items())
        
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

        # store references so we can refresh later
        self.canvas = canvas
        self.center_area = center_area
        self.canvas_window = canvas_window

        # bind resize -> update scroll region
        self.center_area.bind("<Configure>", self._update_scroll_region)
        self.canvas.bind("<Configure>", self._update_scroll_region)

        # initial population
        self.update_items()

    def tkraise(self):
        """Refresh items when the page is brought to front."""
        super().tkraise()
        self.update_items()

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

        # pass the item through to the popup
        img_label.bind("<Button>", lambda e, p=image_path, c=caption, d=description, it=item: HomeImagePopup(self, p, c, d, item=it))

        # Item name
        text_label = ttk.Label(frame, text=caption, font=("Times New Roman",15), wraplength=200)
        text_label.grid(row=1, column=0, sticky="s")

        # Item condition
        condition_text = f"{item.itemCondition}" if item else "N/A"
        condition_label = ttk.Label(frame, text=condition_text, font=("Times New Roman", 9), wraplength=200)
        condition_label.grid(row=2, column=0, sticky="s")

        # Price in larger text
        price_text = f"${item.itemPrice}" if item else "N/A"
        price_label = ttk.Label(frame, text=price_text, font=("Times New Roman", 14, "bold"), wraplength=200)
        price_label.grid(row=3, column=0, sticky="s")

        # Seller name
        seller_name = "Unknown"
        if item:
            seller = UserDatabase.get_user_with_id(item.userID)
            seller_name = seller.name if seller else "Unknown"
        seller_label = ttk.Label(frame, text=f"Seller: {seller_name}", font=("Times New Roman", 9), wraplength=200)
        seller_label.grid(row=4, column=0, sticky="s")

    def _update_scroll_region(self, event=None):
        """Keep the canvas scroll region and width in sync with center_area."""
        try:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))
            self.canvas.itemconfig(self.canvas_window, width=self.canvas.winfo_width())
        except Exception:
            pass

    def update_items(self):
        """Rebuild the center area with current items filtered by category."""
        # clear existing widgets
        for child in self.center_area.winfo_children():
            child.destroy()

        selected_category = self.category_var.get()
        selected_condition = getattr(self, "condition_var", tk.StringVar(value="All")).get()
        images = []
        for item in InventoryDatabase.itemList:
            if getattr(item, "itemStatus", "Available") == "Available":
                # Filter by category
                if selected_category != "All" and getattr(item, "itemCategory", "") != selected_category:
                    continue
                # Filter by condition
                if selected_condition != "All" and getattr(item, "itemCondition", "") != selected_condition:
                    continue
                images.append((
                    item.itemImage,
                    f"{item.itemName}",
                    item.itemDescription,
                    item
                ))

        if images:
            for i, (path, caption, description, item) in enumerate(images):
                self.User_post(self.center_area, path, caption, description, row=i//2, col=i%2, item=item)
        else:
            no_items_label = tk.Label(self.center_area, text="No items found.", font=("Times New Roman", 12), bg="#fafafb")
            no_items_label.grid(row=0, column=0, pady=20)

        # ensure scroll region is updated
        self._update_scroll_region()