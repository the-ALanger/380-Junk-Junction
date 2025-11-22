import tkinter as tk
from tkinter import messagebox
from UserDatabase import UserDatabase
from UserCurrent import UserCurrent

class PagesDelagation:
    def Create_Acc_Data(entry_field1, entry_field2, entry_field3):
        '''
        Create_Acc_Data
        11/11/25
        Sarkis Nazaryan
        
        collects three parameters from the Create Account page entry fields
        and appends them as a new row to the users.csv file. 
        '''
        # 1. Get the string from the Entry widget
        name = entry_field1.get()
        email = entry_field2.get()
        password = entry_field3.get()
        # 2. Open the CSV file in append mode ('a')
        # Use newline='' for proper CSV handling in Python 3
        if not name or not email or not password:
            messagebox.showwarning("Input Error", "Please enter some data before saving.")
            return
        
        try:
            curUser = UserCurrent.check_if_user_exists_by_email(email)
            if curUser:
                messagebox.showwarning("Input Error", "User already exists. Please use a different email.")
                return
            UserDatabase.create_account(name, email, password)
            messagebox.showinfo("Success", f"Data saved: '{name}', '{email}', '{password}'")
            # Optional: Clear the entry field after saving
            entry_field1.delete(0, tk.END) 
            entry_field2.delete(0, tk.END) 
            entry_field3.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("File Error", f"An error occurred while saving data: {e}")

    def combined_functions(entry1, entry2, entry3, controller):
        '''
        combined_functions
        11/11/25
        Sarkis Nazaryan
        
        Combines the actions of passing data to csv
        and switching to sign-in page.
        '''
        PagesDelagation.Create_Acc_Data(entry1, entry2, entry3)
        controller.show_frame("SignInPage")
