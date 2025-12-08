import tkinter as tk
from tkinter import ttk
import csv
import os 

class ImagePopup(tk.Toplevel):
    '''
    ImagePopup
    11/18/25
    Leonel Villanueva

    Popup window class is used to display a larger image of the item that is being viewed as well 
    as its price, caption, and description.
    '''
    def __init__(self, parent, image_path, caption, description):
        super().__init__(parent)
        self.title("Listing Description")
        
        self.csv_path = "0001.csv"
        self.current_username= "You"
        
        # Display Larger Image
        try:
            photo = tk.PhotoImage(file=image_path)
            # Resize image by subsampling (scale down by factor of 2 if too large)
            if photo.width() > 300 or photo.height() > 200:
                scale_x = max(1, photo.width() // 300)
                scale_y = max(1, photo.height() // 200)
                scale = max(scale_x, scale_y)
                photo = photo.subsample(scale, scale)
        except tk.TclError as e:
            print(f"Image load error for '{image_path}': {e}")
            # create a gray placeholder with text
            photo = tk.PhotoImage(width=200, height=150)
            photo.put("gray", to=(0, 0, 200, 150))
        
        img_label = ttk.Label(self, image=photo)
        img_label.image = photo  # keep reference
        img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

        #comment section
        comment_frame = ttk.Frame(self)
        comment_frame.grid(row=0, column=1, sticky="n", padx=20, pady=10)
        tk.Label(comment_frame, text="Comments", font=("Times New Roman",12)).grid(row= 0, column= 0, sticky= "w")
        
        self.comment_display = tk.Text(comment_frame, width = 40, height = 10, state= "disabled", wrap= "word")
        self.comment_display.grid(row= 1, column= 0, pady= (5,10))

        #comment text box
        scrollbar = ttk.Scrollbar(comment_frame, command=self.comment_display.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.comment_display.config(yscrollcommand=scrollbar.set)
        
        self.comment_entry= tk.Text(comment_frame, width= 40, height= 3)
        self.comment_entry.grid(row= 2, column= 0, pady= 5, sticky='w')

        #comment submit button
        submit_button = tk.Button(
        comment_frame,
        text="Submit Comment", 
        width=15,
        command= self.submit_comment
        )
        submit_button.grid(row=3, column=0, sticky="e")

        caption_label = ttk.Label(self, text=caption, font=("Times New Roman",12), wraplength=200)
        caption_label.grid(row=1, column=0, sticky="s")
        
        desc_label = tk.Label(self, text=description, font=("Times New Roman",16), wraplength=400, justify="left")
        desc_label.grid(pady=10, padx=10)

        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.grid(row=2, column=1, sticky="se", padx=10, pady=10)
        
        self.load_comments()

        self.transient(parent)
        self.grab_set()

    def submit_comment(self):
        #save comment to csv 
        comment_text = self.comment_entry.get("1.0", tk.END).strip()
        
        if not comment_text:
            return
        
        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([self.current_username, comment_text])
            
        self.comment_entry.delete("1.0", tk.END)
        self.load_comments()
       
    def load_comments(self):
        self.comment_display.config(state="normal")
        self.comment_display.delete("1.0", tk.END)

        # If file doesnt exist dont submit anything
        if not os.path.exists(self.csv_path):
            self.comment_display.config(state="disabled")
            return

        # Copy comment into csv and in comment section
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    username, comment = row
                    self.comment_display.insert(tk.END, f"{username}: {comment}\n\n")

        self.comment_display.config(state="disabled")