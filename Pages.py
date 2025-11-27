import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.constants import *
from tkinter import messagebox
from UserCurrent import UserCurrent
from UserDatabase import UserDatabase

#---- TODO Refactor This File ----#
'''
    Create_Acc_Data_To_csv
    11/11/25
    Sarkis Nazaryan
    
    collects three parameters from the Create Account page entry fields
    and appends them as a new row to the users.csv file. 
'''
def Create_Acc_Data_To_csv(entry_field1, entry_field2, entry_field3):
    name = entry_field1.get()
    email = entry_field2.get()
    password = entry_field3.get()

    if not name or not email or not password:
        messagebox.showwarning("Input Error", "Please enter some data before saving.")
        return
    
    try:
        curUser = UserCurrent.check_if_user_exists_by_email(email)
        if curUser:
            messagebox.showwarning("Input Error", "User already exists. Please use a different email.")
            return
        UserDatabase.create_account(name, email, password)
        messagebox.showinfo("Success", f"Data saved: '{name}', '{email}', '{password}")
        # Optional: Clear the entry field after saving
        entry_field1.delete(0, tk.END) 
        entry_field2.delete(0, tk.END) 
        entry_field3.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("File Error", f"An error occurred while saving data: {e}")

    
    
#------------------ Application Class ------------------ #
'''
    App
    10/20/25
    Sarkis Nazaryan
    
    App is the main application class that manages different pages.
    It initializes the main window, sets up the frame container,
    and provides a method to switch between different pages.
    '''
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
        for F in (SignInPage, CreateUserPage, HomePage, UserPage):
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
            "CreateUserPage":"800x600"

        }
        geom = sizes.get(page_name)
        if geom:
            self.geometry(geom)
        frame = self.frames[page_name]
        frame.tkraise()
        
#------------------ Sign-In Page ------------------ #
def combine_sign_in(self, entry1, entry2, controller):
        '''
        combine_sign_in
        11/19/25
        Sarkis Nazaryan

        combines the sign-in process by checking user credentials
        and setting the current user if valid.
        '''
        email = entry1.get()
        password = entry2.get()
        ##### user is current user #####
        user = UserCurrent.check_if_user_exists(email, password)
        if user:
            UserCurrent.set_current_user(user)
            ### example on how to access current user info elsewhere ###
            messagebox.showinfo("Login Successful", f"Welcome back, {UserCurrent.current_user.name}!")
            controller.show_frame("HomePage")
        else:
            messagebox.showerror("Sign In Failed", "Invalid email or password.")

class SignInPage(tk.Frame):
    '''
    SignInPage
    11/19/25
    Sarkis Nazaryan

    Class for the sign-in page of the application.
    Contains fields for email and password, and buttons for signing in,
    creating an account, and exiting the app.
    '''
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
                  command=lambda: combine_sign_in(self, e1, e2, controller)).grid(row=2, column=1)
        tk.Button(self, text="Create Account", width=13, 
                  command=lambda: controller.show_frame("CreateUserPage")).grid(row=3, column=1)
        tk.Button(self, text="Exit App", width=10, command=controller.destroy).grid(row=4, column=1, sticky='n')

    '''
    combined_functions
    11/11/25
    Sarkis Nazaryan
    
    Combines the actions of passing data to csv
    and switching to sign-in page.
    '''

def combined_functions(entry1, entry2, entry3, controller):
    Create_Acc_Data_To_csv(entry1, entry2, entry3)
    controller.show_frame("SignInPage")

#------------------ Create-User Page ------------------ #
#page should be create over sign in page and should not destroy it. 
class CreateUserPage(tk.Frame):
    '''
CreateUserPage
11/19/25
Sarkis Nazaryan

Class for the create-user page of the application.
Contains fields for name, email, and password, and buttons for creating an account
'''
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #Labels
        name = tk.Label(self, text="Name").grid(row=0, column=0)
        email = tk.Label(self, text="Email").grid(row=1, column=0)
        password = tk.Label(self, text="Password").grid(row=2, column=0)
        
        #Entries
        name_entry = tk.Entry(self)
        email_entry = tk.Entry(self)
        password_entry = tk.Entry(self, show="*")
        
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        email_entry.grid(row=1, column=1, padx=10, pady=5)
        password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Buttons
        submit_info = tk.Button(
            self,
            text="Create Account",
            width=15,
            command=lambda: combined_functions(name_entry, email_entry, password_entry, controller)
        )
        submit_info.grid(row=3, column=1, pady=10)
        
        return_to_sign_in = tk.Button(
            self,
            text="Return to Sign In",
            width=15,
            command=lambda: controller.show_frame("SignInPage")
        )
        return_to_sign_in.grid(row=4, column=1, pady=5)

#------------------ Pop up window ------------------- #
class ImagePopup(tk.Toplevel):
    '''
    Imagepopup
    11/18/25
    Leonel Villanueva

Popup window class is used to display a larger image of the item that is being viewed as well 
as its price, caption, and description. When this class is called in the HomePage class it creates 
a seperate popup window displaying what picture and info passed to it.
'''
    def __init__(self, parent, image_path, caption, description):
        super().__init__(parent)
        self.title("Listing Description")
        
        # Display Larger Image
        try: 
            photo = tk.PhotoImage(file=image_path)
        except tk.TclError:
            photo = tk.PhotoImage(width=400, height=300)
        
        img_label = ttk.Label(self, image=photo)
        img_label.image = photo  # keep reference
        img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

        text_label = ttk.Label(self, text=caption, font=("Times New Roman",10), wraplength=200)
        text_label.grid(row=1, column=0, sticky="s")
        
        desc_label = tk.Label(self, text=description, wraplength=400, justify="left")
        desc_label.pack(pady=10, padx=10)
        
        
def UserButtonFunction(self, controller):
    
    controller.show_frame("UserPage")
#------------------ Home Page ------------------ #
class HomePage(tk.Frame):
    '''
    HomePage
    11/18/25
    Sarkis, Leonel Villanueva

    Homepage class is responsible for displaying the main interface of the application, 
    it includes the title, side banners, navigation buttons, and a scrollable area
    that displays user posts with images and captions. One data structure that I used in this class
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
        
        #this is the frame that I want to be able to scroll
        center_area = tk.Frame(self, bg="#d0d5dc")

        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='User Page', width=15,
                  command=lambda: controller.show_frame("UserPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='Pop-up', width=15,
                  command=lambda: ImagePopup(self, "images/Charzard.png",
                                     "Caption about charizard",
                                     "This is an example popup description.")).pack(side="bottom", pady=5)
        
        #container Frame
        scroll_container = tk.Frame(self, bg="#2a6cc8")
        scroll_container.pack(fill="both", expand=True)

        #canvas with Scrollbar
        canvas = tk.Canvas(scroll_container, bg="#205fb7", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        #inner frame holds pics
        center_area = tk.Frame(canvas, bg="#fafafb")
        canvas_window = canvas.create_window((0, 0), window=center_area, anchor="nw")
        
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
            #center_area.pack(fill="both", expand=True)
        
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_window, width=canvas.winfo_width())

        center_area.bind("<Configure>", update_scroll_region)
        canvas.bind("<Configure>", update_scroll_region)
        
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

        left_banner = tk.Frame(self, width=50, bg="#585858")
        left_banner.pack(side="left", fill="y")

        right_banner = tk.Frame(self, width=50, bg="#585858")
        right_banner.pack(side="right", fill="y")

        # Use a readonly ttk.Combobox instead of a popup menu
        options = ["Delete Item", "Edit Item"]
        combo_var = tk.StringVar()
        options_combo = ttk.Combobox(self, textvariable=combo_var, values=options, state="readonly")
        options_combo.set("Options")
        options_combo.pack(pady=20)

        def on_option_selected(event):
            choice = combo_var.get()
            if choice == "Delete Item":
                messagebox.showinfo("Action", "Delete Item selected")
                # TODO: wire delete logic to selected item
            elif choice == "Edit Item":
                messagebox.showinfo("Action", "Edit Item selected")
                # TODO: open edit dialog / populate edit form
            # reset combobox to placeholder
            options_combo.set("Options")

        options_combo.bind("<<ComboboxSelected>>", on_option_selected)



        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()

# TODO: Update CSV files after program ends using UpdateCSVs
