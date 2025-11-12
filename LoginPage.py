import tkinter as tk
import csv
from tkinter import messagebox

def Create_Acc_Data_To_csv(entry_field1, entry_field2, entry_field3):
    # 1. Get the string from the Entry widget
    data1 = entry_field1.get()
    data2 = entry_field2.get()
    data3 = entry_field3.get()
    skip = ""
    # 2. Open the CSV file in append mode ('a')
    # Use newline='' for proper CSV handling in Python 3
    if not data1 or not data2 or not data3:
        messagebox.showwarning("Input Error", "Please enter some data before saving.")
        return
    
    try:
        with open('user_inputs.csv', 'a', newline='') as file:
        # 3. Create a CSV writer object
            writer = csv.writer(file)
        # 4. Write the data as a row (a list)
            writer.writerow([skip, data1, data2, data3])
            
            messagebox.showinfo("Success", f"Data saved: '{data1}', '{data2}', '{data3}'")
        # Optional: Clear the entry field after saving
            entry_field1.delete(0, tk.END) 
            entry_field2.delete(0, tk.END) 
            entry_field3.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("File Error", f"An error occurred while saving data: {e}")
    
# # --- Tkinter GUI Setup ---
# window = tk.Tk()
# window.title("CSV Data Entry")
# window.geometry("300x250")



# tk.Label(window, text="Field 1:").grid(row=0, column=0)
# tk.Label(window, text="Field 2:").grid(row=1, column=0)
# tk.Label(window, text="Field 3:").grid(row=2, column=0)

# entry_field1 = tk.Entry(window, width=25)
# entry_field1.grid(row=0, column=1)
# entry_field2 = tk.Entry(window, width=25)
# entry_field2.grid(row=1, column=1)   
# entry_field3 = tk.Entry(window, width=25)
# entry_field3.grid(row=2, column=1)

# # The button calls the save_data_to_csv function
# save_button = tk.Button(window, text="Save to CSV", command=lambda: 
#                         Create_Acc_Data_To_csv(entry_field1 , entry_field2, entry_field3))
# save_button.grid(row=20, column=1, pady=10)

# window.mainloop()

