from email import message
import tkinter as tk
from tkinter import messagebox
from unittest import result
from UserCurrent import UserCurrent
from UserDatabase import UserDatabase

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
        tk.Label(self, text="Name:").grid(row=0, column=0)
        tk.Label(self, text="Email:").grid(row=1, column=0)
        tk.Label(self, text="Password:").grid(row=2, column=0)
        
        #Entries
        self.name_entry = tk.Entry(self)
        self.email_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show="*")
        
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Buttons
        submit_info = tk.Button(
            self,
            text="Create Account",
            width=15,
            command=self.create_and_return
        )
        submit_info.grid(row=3, column=1, pady=10)
        
        return_to_sign_in = tk.Button(
            self,
            text="Return to Sign In",
            width=15,
            command=lambda: controller.show_frame("SignInPage")
        )
        return_to_sign_in.grid(row=4, column=1, pady=5)

    def create_and_return(self):
        '''Create account and return to sign-in page.'''
        result = self.create_acc_data_to_csv(self.name_entry, self.email_entry, self.password_entry)
        if result:
            self.controller.show_frame("SignInPage")

    @staticmethod
    def create_acc_data_to_csv(name_entry, email_entry, password_entry):
        '''Collects data from entry fields and creates a new account.'''
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        noError = True
        errorMessage = ""
        if not name or not email or not password:
            errorMessage = "Input Error", "Please enter some data before saving."
            noError = False
        else:
            curUser = UserCurrent.check_if_user_exists_by_email(email)
            if curUser:
                errorMessage = "Input Error", "User already exists. Please use a different email."
                noError = False
            elif not email.endswith("@my.csun.edu"):
                errorMessage = "Input Error", "Email must be a CSUN email."
                noError = False
            else:
                UserDatabase.create_account(name, email, password)
        if errorMessage:
            messagebox.showerror(errorMessage[0], errorMessage[1])
        else:
            messagebox.showinfo("Success", f"Data saved: '{name}', '{email}'")
        # Clear the entry fields after saving
        name_entry.delete(0, tk.END) 
        email_entry.delete(0, tk.END) 
        password_entry.delete(0, tk.END)
        
        return noError
        
        