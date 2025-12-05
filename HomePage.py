import tkinter as tk
from tkinter import ttk, messagebox  
from InventoryDatabase import InventoryDatabase  
from ImagePopup import ImagePopup

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

        #added description for individual images that show when image is clicked on 
        images = [
            ("images/Charzard.png", "Charizard 1", "This is a super rare limited edition charizard and its worth 67$"),
            ("images/Charzard2.png", "Charizard 2", "This is a super rare limited edition charizard"),
            ("images/Charzard3.png", "Charizard 3", "This is a super rare limited edition charizard"),
            ("images/Charzard4.png", "Charizard 4", "This is a super rare limited edition charizard"),
            ("images/Charzard.png", "Charizard 1", "This is a super rare limited edition charizard"),
            ("images/Charzard2.png", "Charizard 2", "This is a super rare limited edition charizard"),
            ("images/Charzard3.png", "Charizard 3", "This is a super rare limited edition charizard"),
            ("images/Charzard4.png", "Charizard 4", "This is a super rare limited edition charizard"),
        ]

        for i, (path, caption, description) in enumerate(images):
            self.User_post(center_area, path, caption, description, row=i//2, col=i%2)
        
        # for i, item in enumerate(InventoryDatabase.itemList):
        #     if item.itemStatus == "Available":
        #         self.User_post(
        #             center_area,
        #             f"images/{item.itemID}.png",
        #             f"{item.itemName} - ${item.itemPrice}",
        #             row=len(images)//2 + i//2,
        #             col=i%2
        #         )
        
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_window, width=canvas.winfo_width())

        center_area.bind("<Configure>", update_scroll_region)
        canvas.bind("<Configure>", update_scroll_region)

    def User_post(self, parent, image_path, caption, description, row, col):   
        frame = ttk.Frame(parent, padding=10)
        frame.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        frame.columnconfigure(0, weight=1)

        try:
            photo = tk.PhotoImage(file=image_path)
        except tk.TclError:
            photo = tk.PhotoImage(width=200, height=50)  # placeholder

        img_label = ttk.Label(frame, image=photo)
        img_label.image = photo  # keep reference
        img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

        img_label.bind("<Button>", lambda e, p = image_path, c = caption, d = description : ImagePopup(self, p, c, d))

        text_label = ttk.Label(frame, text=caption, font=("Times New Roman",10), wraplength=200)
        text_label.grid(row=1, column=0, sticky="s")