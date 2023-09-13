import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def select_image():
    global selected_image_path
    selected_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    selected_image_label.config(text=f"Selected Image: {os.path.basename(selected_image_path)}")

def add_image():
    if not selected_image_path:
        result_label.config(text="Please select an image first.")
        return
    
    image_name = image_name_entry.get()
    if not image_name:
        result_label.config(text="Please Enter ID with .image extension e.g Peter.jpg, John.png...")
        return
    
    image_data = open(selected_image_path, "rb").read()
    image_path = os.path.join(folder_path, image_name)
    with open(image_path, "wb") as img_file:
        img_file.write(image_data)
    
    result_label.config(text=f"Image '{image_name}' added to folder '{folder_path}'")

folder_path = 'imagesFolder'  # Replace with the folder path where images will be saved

root = Tk()
root.title("Register below")

# Set up the main frame to fill the entire screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
frame = Frame(root, width=width, height=height)
frame.pack(fill=BOTH)

# Content inside the frame
selected_image_path = ""
selected_image_label = Label(frame, text="Selected Image: None", bg="white")
selected_image_label.pack(padx=80, pady=20)

select_button = Button(frame, text="Select Image", command=select_image)
select_button.pack(padx=80, pady=10)

image_name_label = Label(frame, text="Image Name:", bg="white")
image_name_label.pack(padx=80, pady=10)

image_name_entry = Entry(frame)
image_name_entry.pack(padx=80, pady=10)

add_button = Button(frame, text="Add Image", command=add_image)
add_button.pack(padx=80, pady=10)

result_label = Label(frame, text="", bg="white")
result_label.pack(padx=80, pady=10)

root.mainloop()
