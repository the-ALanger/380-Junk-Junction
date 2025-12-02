import tkinter as tk
from SignInPage import SignInPage
from CreateUserPage import CreateUserPage
from HomePage import HomePage
from UserPage import UserPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Junk Junction")
        self.geometry("230x130")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignInPage, CreateUserPage, HomePage, UserPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[page_name] = frame

        self.show_frame("SignInPage")

    def show_frame(self, page_name):
        sizes = {
            "SignInPage": "230x130",
            "HomePage": "800x600",
            "UserPage": "800x600",
            "CreateUserPage": "800x600"
        }
        geom = sizes.get(page_name)
        if geom:
            self.geometry(geom)
        frame = self.frames[page_name]
        
        if page_name == "UserPage":
            frame.refresh_items()
        
        frame.tkraise()