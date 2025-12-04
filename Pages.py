import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.constants import *
import csv
from tkinter import messagebox
from UserCurrent import UserCurrent
import random
from InventoryDatabase import InventoryDatabase

#---- TODO Refactor This File ----#

def Create_Acc_Data_To_csv(entry_field1, entry_field2, entry_field3):
    # 1. Get the string from the Entry widget
    name = entry_field1.get()
    email = entry_field2.get()
    password = entry_field3.get()
    userID = str(random.randint(10000, 99999)) # TODO: Generate a random 5-digit userID that DOES NOT already exist
    # 2. Open the CSV file in append mode ('a')
    # Use newline='' for proper CSV handling in Python 3
    if not name or not email or not password:
        messagebox.showwarning("Input Error", "Please enter some data before saving.")
        return
# import tkinter as tk
# from tkinter import ttk
# from tkinter import *
# from tkinter.constants import *
# from tkinter import messagebox
# from UserCurrent import UserCurrent
# from UserDatabase import UserDatabase
# from InventoryDatabase import InventoryDatabase

# #---- TODO Refactor This File ----#
# '''
#     Create_Acc_Data_To_csv
#     11/11/25
#     Sarkis Nazaryan
    
#     collects three parameters from the Create Account page entry fields
#     and appends them as a new row to the users.csv file. 
# '''
# def Create_Acc_Data_To_csv(entry_field1, entry_field2, entry_field3):
#     name = entry_field1.get()
#     email = entry_field2.get()
#     password = entry_field3.get()

#     if not name or not email or not password:
#         messagebox.showwarning("Input Error", "Please enter some data before saving.")
#         return
    
#     try:
#         curUser = UserCurrent.check_if_user_exists_by_email(email)
#         if curUser:
#             messagebox.showwarning("Input Error", "User already exists. Please use a different email.")
#             return
#         UserDatabase.create_account(name, email, password)
#         messagebox.showinfo("Success", f"Data saved: '{name}', '{email}', '{password}")
#         # Optional: Clear the entry field after saving
#         entry_field1.delete(0, tk.END) 
#         entry_field2.delete(0, tk.END) 
#         entry_field3.delete(0, tk.END)
#     except Exception as e:
#         messagebox.showerror("File Error", f"An error occurred while saving data: {e}")

    
    
# #------------------ Application Class ------------------ #
# '''
#     App
#     10/20/25
#     Sarkis Nazaryan
    
#     App is the main application class that manages different pages.
#     It initializes the main window, sets up the frame container,
#     and provides a method to switch between different pages.
#     '''
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Junk Junction")
#         self.geometry("230x130")

#         container = tk.Frame(self)
#         container.pack(fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)

#         self.frames = {}
#         for F in (SignInPage, CreateUserPage, HomePage, UserPage):
#             page_name = F.__name__
#             frame = F(parent=container, controller=self)
#             frame.grid(row=0, column=0, sticky="nsew")
#             self.frames[page_name] = frame

#         self.show_frame("SignInPage")

#     def show_frame(self, page_name):
#         sizes = {
#             "SignInPage": "230x130",
#             "HomePage": "800x600",
#             "UserPage": "800x600",
#             "CreateUserPage": "800x600"
#         }
#         geom = sizes.get(page_name)
#         if geom:
#             self.geometry(geom)
#         frame = self.frames[page_name]
        
#         # Refresh UserPage items only when switching to it
#         if page_name == "UserPage":
#             frame.refresh_items()
        
#         frame.tkraise()
        
# #------------------ Sign-In Page ------------------ #
# def combine_sign_in(self, entry1, entry2, controller):
#         '''
#         combine_sign_in
#         11/19/25
#         Sarkis Nazaryan

#         combines the sign-in process by checking user credentials
#         and setting the current user if valid.
#         '''
#         email = entry1.get()
#         password = entry2.get()
#         ##### user is current user #####
#         user = UserCurrent.check_if_user_exists(email, password)
#         if user:
#             UserCurrent.set_current_user(user)
#             ### example on how to access current user info elsewhere ###
#             messagebox.showinfo("Login Successful", f"Welcome back, {UserCurrent.current_user.name}!")
#             controller.show_frame("HomePage")
#         else:
#             messagebox.showerror("Sign In Failed", "Invalid email or password.")

# class SignInPage(tk.Frame):
#     '''
#     SignInPage
#     11/19/25
#     Sarkis Nazaryan

#     Class for the sign-in page of the application.
#     Contains fields for email and password, and buttons for signing in,
#     creating an account, and exiting the app.
#     '''
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller

#         tk.Label(self, text="Email").grid(row=0, column=0)
#         tk.Label(self, text="Password").grid(row=1, column=0)

#         e1 = tk.Entry(self)
#         e2 = tk.Entry(self, show="*")
#         e1.grid(row=0, column=1)
#         e2.grid(row=1, column=1)

#         tk.Button(self, text="Sign In", width=10,
#                   command=lambda: combine_sign_in(self, e1, e2, controller)).grid(row=2, column=1)
#         tk.Button(self, text="Create Account", width=13, 
#                   command=lambda: controller.show_frame("CreateUserPage")).grid(row=3, column=1)
#         tk.Button(self, text="Exit App", width=10, command=controller.destroy).grid(row=4, column=1, sticky='n')

#     '''
#     combined_functions
#     11/11/25
#     Sarkis Nazaryan
    
#     Combines the actions of passing data to csv
#     and switching to sign-in page.
#     '''

# def combined_functions(entry1, entry2, entry3, controller):
#     Create_Acc_Data_To_csv(entry1, entry2, entry3)
#     controller.show_frame("SignInPage")

# #------------------ Create-User Page ------------------ #
# #page should be create over sign in page and should not destroy it. 
# class CreateUserPage(tk.Frame):
#     '''
# CreateUserPage
# 11/19/25
# Sarkis Nazaryan

# Class for the create-user page of the application.
# Contains fields for name, email, and password, and buttons for creating an account
# '''
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
        
#         #Labels
#         name = tk.Label(self, text="Name").grid(row=0, column=0)
#         email = tk.Label(self, text="Email").grid(row=1, column=0)
#         password = tk.Label(self, text="Password").grid(row=2, column=0)
        
#         #Entries
#         name_entry = tk.Entry(self)
#         email_entry = tk.Entry(self)
#         password_entry = tk.Entry(self, show="*")
        
        # Display Larger Image
        try: 
            photo = tk.PhotoImage(file=image_path)
        except tk.TclError:
            photo = tk.PhotoImage(width=600, height=450)
        
        img_label = ttk.Label(self, image=photo)
        img_label.image = photo  # keep reference
        img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

        #frame keeping comments on right of image
        comment_frame = ttk.Frame(self)
        comment_frame.grid(row=0, column=1, sticky="n", padx=20, pady=10)

        comments = tk.Label(comment_frame, text="Comments", font=("Times New Roman",12))
        comments.grid(row=0, column=0, sticky="w")

        #comment text box
        comments_entry = tk.Text(comment_frame, width= 40, height= 10)
        comments_entry.grid(row= 1, column= 0, pady= 10, sticky= "w")

        #comment submit button
        submit_info = tk.Button(
        comment_frame,
        text="Submit Comment", 
        width=15,
        command=lambda: combined_functions(comments_entry)
        )
        submit_info.grid(row=2, column=0, sticky="e")

        caption_label = ttk.Label(self, text=caption, font=("Times New Roman",12), wraplength=200)
        caption_label.grid(row=1, column=0, sticky="s")
        
        desc_label = tk.Label(self, text=description, font=("Times New Roman",16), wraplength=400, justify="left")
        desc_label.grid(pady=10, padx=10)

        self.transient(parent)
        self.grab_set_global()

# Between these two classes I have to make it so the pop up button is the photo itself and when the photo is
# clicked it displays a larger version of the photo as well as as a description and price
# once I am able to display the charizard images as well as their description I want to be able to have custom
# inputs that display the actual user images plus their description
#------------------ Home Page ------------------ #
class HomePage(tk.Frame):
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
#         name_entry.grid(row=0, column=1, padx=10, pady=5)
#         email_entry.grid(row=1, column=1, padx=10, pady=5)
#         password_entry.grid(row=2, column=1, padx=10, pady=5)
        
#         # Buttons
#         submit_info = tk.Button(
#             self,
#             text="Create Account",
#             width=15,
#             command=lambda: combined_functions(name_entry, email_entry, password_entry, controller)
#         )
#         submit_info.grid(row=3, column=1, pady=10)
        
#         return_to_sign_in = tk.Button(
#             self,
#             text="Return to Sign In",
#             width=15,
#             command=lambda: controller.show_frame("SignInPage")
#         )
#         return_to_sign_in.grid(row=4, column=1, pady=5)

# #------------------ Pop up window ------------------- #
# class ImagePopup(tk.Toplevel):
#     '''
#     Imagepopup
#     11/18/25
#     Leonel Villanueva

# Popup window class is used to display a larger image of the item that is being viewed as well 
# as its price, caption, and description. When this class is called in the HomePage class it creates 
# a seperate popup window displaying what picture and info passed to it.
# '''
#     def __init__(self, parent, image_path, caption, description):
#         super().__init__(parent)
#         self.title("Listing Description")
        
#         # Display Larger Image
#         try: 
#             photo = tk.PhotoImage(file=image_path)
#         except tk.TclError:
#             photo = tk.PhotoImage(width=400, height=300)
        
#         img_label = ttk.Label(self, image=photo)
#         img_label.image = photo  # keep reference
#         img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

#         text_label = ttk.Label(self, text=caption, font=("Times New Roman",10), wraplength=200)
#         text_label.grid(row=1, column=0, sticky="s")
        
#         desc_label = tk.Label(self, text=description, wraplength=400, justify="left")
#         desc_label.pack(pady=10, padx=10)
        
        
# def UserButtonFunction(self, controller):
    
#     controller.show_frame("UserPage")
# #------------------ Home Page ------------------ #
# class HomePage(tk.Frame):
#     '''
#     HomePage
#     11/18/25
#     Sarkis, Leonel Villanueva

#     Homepage class is responsible for displaying the main interface of the application, 
#     it includes the title, side banners, navigation buttons, and a scrollable area
#     that displays user posts with images and captions. One data structure that I used in this class
#     '''

    
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller

#         title = tk.Label(self, text='Junk Junction', bg="#791919", fg="white",
#                          font=("Times New Roman", 20), anchor="center")
#         title.pack(fill="x", side="top")

#         left_banner = tk.Frame(self, width=50, bg="#312b2b")
#         left_banner.pack(side="left", fill="y")

#         right_banner = tk.Frame(self, width=50, bg="#312b2b")
#         right_banner.pack(side="right", fill="y") 
        
        #this is the frame that I want to be able to scroll
        center_area = tk.Frame(self, bg="#d0d5dc")

        tk.Button(self, text='Log Out', width=15,
                  command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
        tk.Button(self, text='User Page', width=15,
                  command=lambda: controller.show_frame("UserPage")).pack(side="bottom", pady=5)
#         #this is the frame that I want to be able to scroll
#         center_area = tk.Frame(self, bg="#d0d5dc")

#         tk.Button(self, text='Log Out', width=15,
#                   command=lambda: controller.show_frame("SignInPage")).pack(side="bottom", pady=5)
#         tk.Button(self, text='User Page', width=15,
#                   command=lambda: controller.show_frame("UserPage")).pack(side="bottom", pady=5)
#         tk.Button(self, text='Pop-up', width=15,
#                   command=lambda: ImagePopup(self, "images/Charzard.png",
#                                      "Caption about charizard",
#                                      "This is an example popup description.")).pack(side="bottom", pady=5)
        
#         #container Frame
#         scroll_container = tk.Frame(self, bg="#2a6cc8")
#         scroll_container.pack(fill="both", expand=True)

#         #canvas with Scrollbar
#         canvas = tk.Canvas(scroll_container, bg="#205fb7", highlightthickness=0)
#         canvas.pack(side="left", fill="both", expand=True)

#         scrollbar = tk.Scrollbar(scroll_container, orient="vertical", command=canvas.yview)
#         scrollbar.pack(side="right", fill="y")

#         canvas.configure(yscrollcommand=scrollbar.set)

#         #inner frame holds pics
#         center_area = tk.Frame(canvas, bg="#fafafb")
#         canvas_window = canvas.create_window((0, 0), window=center_area, anchor="nw")
        
        for i in range(2):
            center_area.columnconfigure(i, weight=1, uniform="col")
            center_area.rowconfigure(i, weight=1, uniform="row")

        images = []

        #TODO: implement dynamic images
        for item in InventoryDatabase.itemList[1:]:
            images.append(["images/Charzard.png", item.itemName, item.itemDescription])
#         for i in range(2):
#             center_area.columnconfigure(i, weight=1, uniform="col")
#             center_area.rowconfigure(i, weight=1, uniform="row")
        
        #added description for individual images that show when image is clicked on

        for i, (path, caption, description) in enumerate(images):
            self.User_post(center_area, path, caption, description, row=i//2, col=i%2)
#         images = [
#             ("images/Charzard.png", "bro"),
#             ("images/Charzard2.png", "this"),
#             ("images/Charzard3.png", "is"),
#             ("images/Charzard4.png", "charizard"),
#             ("images/Charzard.png", "bro"),
#             ("images/Charzard2.png", "this"),
#             ("images/Charzard3.png", "is"),
#             ("images/Charzard4.png", "charizard"),
#         ]

#         for i, (path, text) in enumerate(images):
#             self.User_post(center_area, path, text, row=i//2, col=i%2)
#             #center_area.pack(fill="both", expand=True)
        
#         for item in InventoryDatabase.itemList:
#             if item.itemStatus == "Available":
#                 self.User_post(
#                     center_area,
#                     f"images/{item.itemID}.png",  # Assuming images are named by itemID
#                     f"{item.itemName} - ${item.itemPrice}",
#                     row=len(images)//2 + InventoryDatabase.itemList.index(item)//2,
#                     col=InventoryDatabase.itemList.index(item)%2
#                     tk.Button(self, text="View Details",
#                               command=lambda messagebox.showinfo("Item Details",
#                                                           f"Name: {item.itemName}\n"
#                                                           f"Description: {item.itemDescription}\n"
#                                                           f"Condition: {item.itemCondition}\n"
#                                                           f"Category: {item.itemCategory}\n"
#                                                           f"Price: ${item.itemPrice}\n"
#                                                           f"Status: {item.itemStatus}")).grid(row=len(images)//2 + InventoryDatabase.itemList.index(item)//2,
#                                                                                              column=InventoryDatabase.itemList.index(item)%2))
                
#         def update_scroll_region(event=None):
#             canvas.configure(scrollregion=canvas.bbox("all"))
#             canvas.itemconfig(canvas_window, width=canvas.winfo_width())

#         center_area.bind("<Configure>", update_scroll_region)
#         canvas.bind("<Configure>", update_scroll_region)
        

        
#     def User_post(self, parent, image_path, caption, row, col):   
#         frame = ttk.Frame(parent, padding=10)
#         frame.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
#         frame.columnconfigure(0, weight=1)

#         try:
#             photo = tk.PhotoImage(file=image_path)
#         except tk.TclError:
#             photo = tk.PhotoImage(width=200, height=50)  # placeholder

#         img_label = ttk.Label(frame, image=photo)
#         img_label.image = photo  # keep reference
#         img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

#         text_label = ttk.Label(frame, text=caption, font=("Times New Roman",10), wraplength=200)
#         text_label.grid(row=1, column=0, sticky="s")

# #------------------ User Page ------------------ #

# class UserPage(tk.Frame):
    
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         self.controller = controller
#         self.items_frame = None
        
#     def refresh_items(self):
#         """Refresh the page when user logs in."""
#         # Clear previous widgets
#         for widget in self.winfo_children():
#             widget.destroy()
        
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

#------------------ User Page ------------------ #
class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
#         # Get items for current user
#         user_id = UserCurrent.get_current_user_id()
        
#         if not user_id:
#             messagebox.showwarning("Error", "No user logged in.")
#             self.controller.show_frame("SignInPage")
#             return
            
#         items = InventoryDatabase.get_items_with_user_id(user_id)

#         # Create a button for each item
#         title = tk.Label(self, text=f"Your Items", font=("Times New Roman", 14))
#         title.pack(pady=10)
        
#         if items:
#             for item in items:
#                 # ItemInfo has attributes like item.itemName
#                 btn = tk.Button(self, text=item.itemName,
#                                command=lambda i=item: self.on_item_click(i))
#                 btn.pack(pady=5)
#         else:
#             tk.Label(self, text="No items found.").pack(pady=10)
        
#         # Log out button
#         tk.Button(self, text='Log Out', width=15,
#                   command=lambda: self.controller.show_frame("SignInPage")).pack(side="bottom", pady=10)

#     def on_item_click(self, item):
#         # handle item button click
#         messagebox.showinfo("Item", f"You clicked: {item.itemName}")

#     #TODO: Add dropdown on each button to edit/delete/ item
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

# # TODO: Update CSV files after program ends using UpdateCSVs
