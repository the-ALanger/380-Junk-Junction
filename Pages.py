import tkinter as tk
from tkinter import *
from tkinter.constants import *
import csv
from tkinter import messagebox

def CreateAcc_Data_To_csv(entry_field1, entry_field2, entry_field3):
    # 1. Get the string from the Entry widget
    data1 = entry_field1.get()
    data2 = entry_field2.get()
    data3 = entry_field3.get()
    IDskip = ""
    # 2. Open the CSV file in append mode ('a')
    # # Use newline='' for proper CSV handling in Python 3
    if not data1 or not data2 or not data3:
        messagebox.showwarning("Input Error", "Please enter some data before saving.")
        return
        
    try:
        with open('user_inputs.csv', 'a', newline='') as file:
        # 3. Create a CSV writer object
            writer = csv.writer(file)
        # 4. Write the data as a row (a list)
            writer.writerow([IDskip, data1, data2, data3])
                
            messagebox.showinfo("Success", f"Data saved: '{data1}', '{data2}', '{data3}'")
            # Clear the entry field after saving
            entry_field1.delete(0, tk.END) 
            entry_field2.delete(0, tk.END) 
            entry_field3.delete(0, tk.END)
    except Exception as e:
         messagebox.showerror("File Error", f"An error occurred while saving data: {e}")

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
        for F in (SignInPage, CreateUser_Page, HomePage, UserPage):
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
            "CreateUser_Page":"800x600"

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
                  command=lambda: controller.show_frame("HomePage")).grid(row=2, column=1)
        tk.Button(self, text="Create Account", width=10, 
                  command=lambda: controller.show_frame("CreateUser_Page")).grid(row=3, column=1)
        tk.Button(self, text="Exit App", width=10, command=controller.destroy).grid(row=4, column=1, sticky='n')

        
#------------------ Create-User Page ------------------ #
class CreateUser_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        tk.Label(self, text="Name").grid(row=0, column=0)
        tk.Label(self, text="Email").grid(row=1, column=0)
        tk.Label(self, text="Password").grid(row=2, column=0)
        
        e1 = tk.Entry(self).grid(row=0, column=1)
        e2 = tk.Entry(self).grid(row=1, column=1) 
        e3 = tk.Entry(self, show="*").grid(row=2, column=1)
        
        submit_info = tk.Button(self, text="Create Account", width=15, command=lambda: (self.CreateAcc_Data_To_csv(e1, e2, e3),
                                controller.show_frame("SignInPage")))
        submit_info.grid(row=3, column=1)

#------------------ Home Page ------------------ #
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text='Junk Junction', bg="#791919", fg="white",
                         font=("Times New Roman", 20), anchor="center")
        title.pack(fill="x", side="top")

        left_banner = tk.Frame(self, width=50, bg="#585858")
        left_banner.pack(side="left", fill="y")

        right_banner = tk.Frame(self, width=50, bg="#585858")
        right_banner.pack(side="right", fill="y")
        
        center_area = tk.Frame(self, bg="#f0f0f0")

        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='User Page', width=15,
                  command=lambda: controller.show_frame("UserPage")).pack(side="bottom", pady=5)
    
#------------------ User Page ------------------ #
class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        title = tk.Label(self, text='User Page', bg="#791919", fg="white",
                         font=("Times New Roman", 20), anchor="center")
        title.pack(fill="x", side="top")

        left_banner = tk.Frame(self, width=50, bg="#585858")
        left_banner.pack(side="left", fill="y")

        right_banner = tk.Frame(self, width=50, bg="#585858")
        right_banner.pack(side="right", fill="y")

        tk.Button(self, text="Home Page", width=15,
                  command=lambda: controller.show_frame("HomePage")).pack(side="bottom", pady=5)
        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="left", pady=5)

if __name__ == "__main__":
    app = App()
    app.mainloop()