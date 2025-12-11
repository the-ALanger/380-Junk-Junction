from CreateUserPage import CreateUserPage
import tkinter as tk

def test_create_user_page_initialization():
    root = tk.Tk()
    controller = tk.Frame(root)
    create_user_page = CreateUserPage(parent=controller, controller=controller)
    
    assert isinstance(create_user_page, CreateUserPage)
    assert create_user_page.controller == controller
    assert create_user_page.winfo_class() == "Frame"
    
    root.destroy()
    
def test_create_acc_data_to_csv():
    result = CreateUserPage.create_acc_data_to_csv(
        name_entry=tk.Entry().insert(0, "Test User"),
        email_entry=tk.Entry().insert(0, "test@gmail.com"),
        password_entry=tk.Entry().insert(0, "password")
    )
    assert result == True

def test_create_acc_data_to_csv_empty_fields():
    result = CreateUserPage.create_acc_data_to_csv(
        name_entry=tk.Entry().insert(0, ""),
        email_entry=tk.Entry().insert(0, ""),
        password_entry=tk.Entry().insert(0, "")
    )
    assert result == False 
    
def test_create_acc_data_to_csv_existing_user():
    result = CreateUserPage.create_acc_data_to_csv(
        name_entry=tk.Entry().insert(0, "Existing User"),
        email_entry=tk.Entry().insert(0, "existing@gmail.com"),
        password_entry=tk.Entry().insert(0, "password")
    )
    assert result == False
