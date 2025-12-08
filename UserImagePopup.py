import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from UserCurrent import UserCurrent
from UserDatabase import UserDatabase
from InventoryDatabase import InventoryDatabase

class UserImagePopup(tk.Toplevel):
    '''
    ImagePopup
    11/18/25
    Leonel Villanueva

    Popup window class is used to display a larger image of the item that is being viewed as well 
    as its price, caption, and description.
    '''
    def __init__(self, parent, image_path, caption, description, item=None):
        super().__init__(parent)
        self.title("Listing Description")
        self.item = item

        self.current_username = UserCurrent.current_user.name or "Anonymous"

        try:
            photo = tk.PhotoImage(file=image_path)
            # Resize image by subsampling (scale down by factor if too large)
            if photo.width() > 350 or photo.height() > 250:
                scale_x = max(1, photo.width() // 350)
                scale_y = max(1, photo.height() // 250)
                scale = max(scale_x, scale_y)
                photo = photo.subsample(scale, scale)
        except tk.TclError as e:
            print(f"Image load error for '{image_path}': {e}")
            # Create a gray placeholder with text
            photo = tk.PhotoImage(width=350, height=250)
            photo.put("gray", to=(0, 0, 350, 250))
        
        img_label = ttk.Label(self, image=photo)
        img_label.image = photo  # keep reference
        img_label.grid(row=0, column=0, sticky="n", pady=(0,5))

        # comment section (display + entry) on right of image
        comment_frame = ttk.Frame(self)
        comment_frame.grid(row=0, column=1, sticky="n", padx=20, pady=10)
        tk.Label(comment_frame, text="Comments", font=("Times New Roman",12)).grid(row=0, column=0, sticky="w")
        
        # display for existing comments
        self.comment_display = tk.Text(comment_frame, width=40, height=10, state="disabled", wrap="word")
        self.comment_display.grid(row=1, column=0, pady=(5,10))

        self.comment_display.tag_configure("username", font=("Times New Roman", 10, "bold"))

        # entry for new comment
        self.comment_entry = tk.Text(comment_frame, width=40, height=3)
        self.comment_entry.grid(row=2, column=0, pady=5, sticky='w')

        # comment submit button
        submit_button = tk.Button(comment_frame, text="Submit Comment", width=15,
                                  command=lambda: self.submit_comment(self.comment_entry))
        submit_button.grid(row=3, column=0, sticky="e")

        # Caption, price and seller on the left under the image (same formatting)
        caption_label = ttk.Label(self, text=caption, font=("Times New Roman",12), wraplength=400)
        caption_label.grid(row=1, column=0, sticky="w", padx=10)

        # Price (larger)
        price_text = f"${getattr(self.item, 'itemPrice', 'N/A')}" if self.item else "N/A"
        price_label = ttk.Label(self, text=price_text, font=("Times New Roman", 14, "bold"), wraplength=400)
        price_label.grid(row=2, column=0, sticky="w", padx=10, pady=(2,2))

        # Item condition (displayed below the price)
        condition_text = f"{getattr(self.item, 'itemCondition', 'N/A')}" if self.item else "N/A"
        condition_label = ttk.Label(self, text=condition_text, font=("Times New Roman", 10), wraplength=400)
        condition_label.grid(row=3, column=0, sticky="w", padx=10)

        seller_name = "Unknown"
        if self.item:
            seller = UserDatabase.get_user_with_id(getattr(self.item, "userID", None))
            seller_name = getattr(seller, "name", "Unknown")
        seller_label = ttk.Label(self, text=f"Seller: {seller_name}", font=("Times New Roman", 10), wraplength=400)
        seller_label.grid(row=4, column=0, sticky="w", padx=10)

        self.seller_name = seller_name

        desc_label = tk.Label(self, text=description, font=("Times New Roman",12), wraplength=400, justify="left")
        desc_label.grid(row=5, column=0, pady=10, padx=10)

        close_button = tk.Button(self, text="Close", command=self.destroy)
        close_button.grid(row=6, column=1, sticky="se", padx=10, pady=10)

        # load comment history into display
        self.load_comments()

        self.transient(parent)
        self.grab_set()

    def submit_comment(self, comments_entry):
        """Save comment to the CSV path stored on the item (fallback to default file)."""
        comment_text = comments_entry.get("1.0", tk.END).strip()
        if not comment_text:
            return

        csv_path = getattr(self.item, "itemComments", None) or f"ItemComments/comments{getattr(self.item, 'itemID', '0000')}.csv"
        csv_path = os.path.normpath(csv_path)

        csv_dir = os.path.dirname(csv_path) or "ItemComments"
        os.makedirs(csv_dir, exist_ok=True)

        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([self.current_username, comment_text])

        comments_entry.delete("1.0", tk.END)
        self.load_comments()
       
    def load_comments(self):
        """Load comments from the CSV path stored on the item (fallback to default file)."""
        self.comment_display.config(state="normal")
        self.comment_display.delete("1.0", tk.END)

        csv_path = getattr(self.item, "itemComments", None) or f"ItemComments/comments{getattr(self.item, 'itemID', '0000')}.csv"
        csv_path = os.path.normpath(csv_path)

        if not os.path.exists(csv_path):
            self.comment_display.config(state="disabled")
            return

        current_user_name = getattr(UserCurrent.current_user, "name", None)

        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    username, comment = row[0], row[1]
                    # Determine suffix:
                    if username == self.seller_name and current_user_name and username == current_user_name:
                        suffix = "(You)"
                    elif username == self.seller_name:
                        suffix = "(Seller)"
                    else:
                        suffix = ""

                    name_block = f"{username}{suffix}"
                    start_index = self.comment_display.index(tk.END)
                    self.comment_display.insert(tk.END, name_block)
                    end_index = self.comment_display.index(tk.END)
                    self.comment_display.tag_add("username", start_index, end_index)

                    self.comment_display.insert(tk.END, f": {comment}\n\n")

        self.comment_display.config(state="disabled")

    def unlist_item(self):
        """Unlist the item from inventory."""
        if not self.item:
            messagebox.showwarning("Error", "Item not found.")
            return
        
        if messagebox.askyesno("Confirm", f"Unlist '{self.item.itemName}'?"):
            try:
                InventoryDatabase.make_unlisted(self.item)
                messagebox.showinfo("Success", "Item unlisted successfully.")
                self.destroy()
                # refresh parent (UserPage) listing
                try:
                    self.parent.refresh_items()
                except Exception:
                    pass
            except Exception as e:
                messagebox.showerror("Error", f"Failed to unlist item: {e}")

    def sell_item(self):
        """Sell the item from inventory."""
        if not self.item:
            messagebox.showwarning("Error", "Item not found.")
            return
        
        if messagebox.askyesno("Confirm", f"Sell '{self.item.itemName}'?"):
            try:
                InventoryDatabase.make_sold(self.item)
                messagebox.showinfo("Success", "Item sold successfully.")
                self.destroy()
                try:
                    self.parent.refresh_items()
                except Exception:
                    pass
            except Exception as e:
                messagebox.showerror("Error", f"Failed to sell item: {e}")