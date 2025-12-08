import tkinter as tk
from tkinter import messagebox
from UserCurrent import UserCurrent

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
        
        # Set window size
        controller.geometry("600x500")

        tk.Label(self, text="Email").grid(row=0, column=0)
        tk.Label(self, text="Password").grid(row=1, column=0)

        e1 = tk.Entry(self)
        e2 = tk.Entry(self, show="*")
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)

        tk.Button(self, text="Sign In", width=10,
                  command=lambda: self.combine_sign_in(e1, e2)).grid(row=2, column=1)
        tk.Button(self, text="Create Account", width=13, 
                  command=lambda: controller.show_frame("CreateUserPage")).grid(row=3, column=1)
        tk.Button(self, text="Exit App", width=10, command=controller.destroy).grid(row=4, column=1, sticky='n')

    def combine_sign_in(self, entry1, entry2):
        '''
        combine_sign_in
        11/19/25
        Sarkis Nazaryan

        combines the sign-in process by checking user credentials
        and setting the current user if valid.
        '''
        email = entry1.get()
        password = entry2.get()
        user = UserCurrent.check_if_user_exists(email, password)
        if user:
            UserCurrent.set_current_user(user)
            messagebox.showinfo("Login Successful", f"Welcome back, {UserCurrent.current_user.name}!")
            self.controller.show_frame("HomePage")
        else:
            messagebox.showerror("Sign In Failed", "Invalid email or password.")