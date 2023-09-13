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
folder_path = 'imagesFolder'  
root = Tk()
root.title("Register data")
root.configure(bg="#00008B")  
frame = Frame(root, bg="#00008B")
frame.grid(row=0, column=0, padx=50, pady=50)
title_label = Label(frame, text="Register New Data below", font=("Helvetica", 20, "bold"), fg="white", bg="#00008B")
title_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="w") 

selected_image_path = ""
selected_image_label = Label(frame, text="Selected Image: None", bg="#00008B", fg="white")
selected_image_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")  

select_button = Button(frame, text="Select Image", command=select_image, width=20)
select_button.grid(row=2, column=0, padx=10, pady=5, sticky="w")  

image_name_label = Label(frame, text="Image Name:", bg="#00008B", fg="white")
image_name_label.grid(row=3, column=0, padx=10, pady=5, sticky="w") 
image_name_entry = Entry(frame, width=20)
image_name_entry.grid(row=3, column=1, padx=1, pady=5, sticky="w")  

add_button = Button(frame, text="Add Image", command=add_image, width=20)
add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w") 
result_label = Label(frame, text="", bg="#00008B", fg="white")
result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w") 
root.mainloop()
