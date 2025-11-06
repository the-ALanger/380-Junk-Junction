import tkinter as tk
import csv
from tkinter import messagebox

def save_data_to_csv():
    # 1. Get the string from the Entry widget
    user_input1 = entry_field1.get()
    user_input2 = entry_field2.get()

    if not user_input1 or not user_input2:
        messagebox.showwarning("Warning", "Please enter some data.")
        return

    # 2. Open the CSV file in append mode ('a')
    # Use newline='' for proper CSV handling in Python 3
    try:
        with open('user_inputs.csv', 'a', newline='') as file:
            # 3. Create a CSV writer object
            writer = csv.writer(file)

            # 4. Write the data as a row (a list)
            writer.writerow([user_input1, user_input2])
            
        messagebox.showinfo("Success", f"Data saved: '{user_input1}', '{user_input2}'")
        # Optional: Clear the entry field after saving
        entry_field1.delete(0, tk.END) 
        entry_field2.delete(0, tk.END)
    except IOError as e:
        messagebox.showerror("Error", f"Could not write to file: {e}")

# --- Tkinter GUI Setup ---
window = tk.Tk()
window.title("CSV Data Entry")
window.geometry("300x150")

label = tk.Label(window, text="Enter a string:")
label.pack(pady=10)

entry_field1 = tk.Entry(window, width=25)
entry_field1.pack(pady=5)

entry_field2 = tk.Entry(window, width=25)
entry_field2.pack(pady=5)

# The button calls the save_data_to_csv function
save_button = tk.Button(window, text="Save to CSV", command=save_data_to_csv)
save_button.pack(pady=20)

window.mainloop()

