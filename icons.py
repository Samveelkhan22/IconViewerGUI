from tkinter import Tk, Label, Entry, Button, messagebox, LabelFrame
from PIL import Image, ImageTk
import os

# Path to your dataset directory containing the icon images
dataset_dir = r"C:\Users\J.I Traders\Downloads\icon_folder"

# Function to search for the image file based on the prompt
def search_icon():
    prompt = entry.get()
    for file_name in os.listdir(dataset_dir):
        # Remove file extension and convert to lowercase for case-insensitive comparison
        name = os.path.splitext(file_name)[0].lower()
        if prompt.lower() in name:
            return os.path.join(dataset_dir, file_name)
    return None

# Function to display the icon image
def display_icon():
    icon_path = search_icon()

    if icon_path is not None:
        image = Image.open(icon_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        label.configure(image=photo)
        label.image = photo
        label.pack()
    else:
        messagebox.showinfo("Icon Not Found", "Icon not found for the given prompt.")

# Create the main window
window = Tk()
window.title("Icon Viewer")
window.configure(bg="#F8F8F8")  # Set background color

# Create a frame for the input section
input_frame = LabelFrame(window, text="Enter Icon Name", font=("Arial", 14), padx=20, pady=20, bg="#F8F8F8")
input_frame.pack(padx=50, pady=50)

# Create the label, entry, and button widgets inside the input frame
entry = Entry(input_frame, width=30, font=("Arial", 14))
entry.pack(pady=10)

def on_button_click():
    display_icon()

button = Button(input_frame, text="Search", font=("Arial", 14), bg="#4CAF50", fg="#FFFFFF", activebackground="#45a049", bd=0, padx=10, pady=5, cursor="hand2", command=on_button_click)
button.pack(pady=10)

# Create a frame for the image display
image_frame = LabelFrame(window, text="Icon Image", font=("Arial", 14), padx=20, pady=20, bg="#F8F8F8")
image_frame.pack(padx=50, pady=50)

# Create the label widget inside the image frame to display the icon image
label = Label(image_frame, bg="#FFFFFF")

# Start the GUI event loop
window.mainloop()
