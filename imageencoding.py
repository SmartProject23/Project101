import cv2
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
from tkinter import Tk
from tkinter import filedialog

# Load the pre-trained VGG16 model
model = VGG16(weights='imagenet', include_top=False)

def encode_image(image_path):
    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # Get the features from the VGG16 model
    features = model.predict(img)
    return features.flatten()

if __name__ == "__main__":
    # Initialize a Tkinter window
    root = Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user to select an image file
    image_path = filedialog.askopenfilename(title="Select an Image")

    if image_path:
        try:
            encodings = encode_image(image_path)
            print("Image Encodings:")
            print(encodings)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No image selected.")
