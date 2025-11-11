import tkinter as tk
from tkinter import ttk
from tkinter.constants import *

#------------------ Application Class ------------------ #
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Junk Junction")
        self.geometry("230x130")  # start size for sign-in

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignInPage, HomePage, UserPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page_name] = frame

        self.show_frame("SignInPage")

    def show_frame(self, page_name):
        # map page to desired window geometry
        sizes = {
            "SignInPage": "230x130",
            "HomePage": "800x600",
            "UserPage": "800x600",
        }
        geom = sizes.get(page_name)
        if geom:
            self.geometry(geom)
        frame = self.frames[page_name]
        frame.tkraise()
        
#------------------ Sign-In Page ------------------ #
class SignInPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Email").grid(row=0, column=0)
        tk.Label(self, text="Password").grid(row=1, column=0)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self, show="*")
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        tk.Button(self, text="Sign In", width=10,
                  command=lambda: controller.show_frame("HomePage")).grid(row=2, column=1, pady=10)
        tk.Button(self, text="Exit App", width=10, command=controller.destroy).grid(row=3, column=1)

#------------------ Home Page ------------------ #
class HomePage(tk.Frame):
    
    #tk.Tk().rowconfigure(0, weight = 1)
    #tk.Tk().columnconfigure(0, weight = 1)
    
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
        
        #this is the frame that I want to be able to scroll
        center_area = tk.Frame(self, bg="#d0d5dc")

        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='User Page', width=15,
                  command=lambda: controller.show_frame("UserPage")).pack(side="bottom", pady=5)
       
        for i in range(2):
            center_area.columnconfigure(i, weight=1, uniform="col")
            center_area.rowconfigure(i, weight=1, uniform="row")
        

        images = [
            ("images/Charzard.png", "bro"),
            ("images/Charzard2.png", "this"),
            ("images/Charzard3.png", "is"),
            ("images/Charzard4.png", "charizard"),
            ("images/Charzard.png", "bro"),
            ("images/Charzard2.png", "this"),
            ("images/Charzard3.png", "is"),
            ("images/Charzard4.png", "charizard"),
        ]

        for i, (path, text) in enumerate(images):
            self.User_post(center_area, path, text, row=i//2, col=i%2)
            center_area.pack(fill="both", expand=True)
        
    def User_post(self, parent, image_path, caption, row, col):   
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

        text_label = ttk.Label(frame, text=caption, font=("Times New Roman",10), wraplength=200)
        text_label.grid(row=1, column=0, sticky="s")

            
#------------------ User Page ------------------ #
class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        title = tk.Label(self, text='User Page', bg="#791919", fg="white",
                         font=("Times New Roman", 20), anchor="center")
        title.pack(fill="x", side="top")

        left_banner = tk.Frame(self, width=50, bg="#312b2b")
        left_banner.pack(side="left", fill="y")

        right_banner = tk.Frame(self, width=50, bg="#312b2b")
        right_banner.pack(side="right", fill="y")

        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text="Home Page", width=15,
                  command=lambda: controller.show_frame("HomePage")).pack(side="bottom", pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()