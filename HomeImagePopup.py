import tkinter as tk
from tkinter import ttk

class HomeImagePopup(tk.Toplevel):
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
        
        # Display Larger Image
        try:
            photo = tk.PhotoImage(file=image_path)
            # Resize image by subsampling (scale down by factor of 2 if too large)
            if photo.width() > 300 or photo.height() > 2000:
                scale_x = max(1, photo.width() // 300)
                scale_y = max(1, photo.height() // 200)
                scale = max(scale_x, scale_y)
                photo = photo.subsample(scale, scale)
        except tk.TclError as e:
            print(f"Image load error for '{image_path}': {e}")
            # Create a gray placeholder with text
            photo = tk.PhotoImage(width=300, height=200)
            photo.put("gray", to=(0, 0, 300, 200))
        
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
        command=lambda: self.submit_comment(comments_entry)
        )
        submit_info.grid(row=2, column=0, sticky="e")

        caption_label = ttk.Label(self, text=caption, font=("Times New Roman",12), wraplength=200)
        caption_label.grid(row=1, column=0, sticky="s")
        
        desc_label = tk.Label(self, text=description, font=("Times New Roman",16), wraplength=400, justify="left")
        desc_label.grid(pady=10, padx=10)

        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.grid(row=2, column=1, sticky="se", padx=10, pady=10)

        self.transient(parent)
        self.grab_set()

    def submit_comment(self, comments_entry):
        """Handle comment submission"""
        comment_text = comments_entry.get("1.0", tk.END).strip()
        if comment_text:
            print(f"Comment submitted: {comment_text}")
            comments_entry.delete("1.0", tk.END)
        else:
            print("Empty comment")
