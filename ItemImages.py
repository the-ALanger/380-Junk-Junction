import tkinter as tk
import csv

################################################ CAN & SHOULD be its own class (ie TEMP) ##############################################
# Load CSV into a 2D list
image_data = []
with open("JJItemImages.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip header row
    for row in reader:
        image_data.append(row)

# Find the row with item_ID 1001
image_paths = []
for row in image_data:
    if row[0].strip() == "1001":                   ############  CHANGE ITEM ID HERE
        image_paths = [cell.strip() for cell in row[1:]]  # Skip item_ID column
        break

################################################ Slideshow Display ##############################################
# Initialize Tkinter window
root = tk.Tk()
root.title("Image Slideshow from CSV")

# Load images
photos = [tk.PhotoImage(file=path) for path in image_paths]

# Create label to display images
image_label = tk.Label(root)
image_label.pack()

# Slideshow logic
current_index = 0
def update_image():
    global current_index
    image_label.config(image=photos[current_index])
    current_index = (current_index + 1) % len(photos)
    root.after(2000, update_image)  # Change every 2 seconds

# Start slideshow
update_image()

root.mainloop()

############################################## Side-by-Side Display ##############################################
# Load CSV into a 2D list
image_data = []
with open("JJItemImages.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip header row
    for row in reader:
        image_data.append(row)

# Find the row with item_ID 1001
image_paths = []
for row in image_data:
    if row[0].strip() == "1001":
        image_paths = [cell.strip() for cell in row[1:]]  # Skip item_ID column
        break

# Initialize Tkinter window
root = tk.Tk()
root.title("Side-by-Side Image Display")

# Create a frame to hold the images horizontally
frame = tk.Frame(root)
frame.pack()

# Load and display each image side-by-side
photos = []
for path in image_paths:
    photo = tk.PhotoImage(file=path)
    photos.append(photo)
    label = tk.Label(frame, image=photo)
    label.pack(side=tk.LEFT, padx=5)

root.mainloop()
