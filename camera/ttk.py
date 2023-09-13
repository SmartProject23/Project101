# import tkinter as tk

# # Create the main window
# root = tk.Tk()
# root.title("Button with Image")

# # Load the image
# image = tk.PhotoImage(file="path_to_image.png")  # Replace with the path to your image

# # Create a button with an image
# button = tk.Button(root, image=image, command=lambda: print("Button"))
# button.pack()

# # Start the tkinter main loop
# root.mainloop()

# RESIZING IMAGE



import tkinter as tk
import cv2

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")

        # Create a label to display the camera feed
        self.label = tk.Label(root)
        self.label.pack()

        # Create a quit button
        self.quit_button = tk.Button(root, text="Quit", command=self.close_camera)
        self.quit_button.place(x=10, y=10)  # Adjust the position as needed

        self.is_camera_active = True  # Camera is active by default
        self.camera = cv2.VideoCapture(0)  # Open the default camera (0)

        self.update()

    def close_camera(self):
        self.is_camera_active = False
        self.root.destroy()  # Close the application

    def update(self):
        if self.is_camera_active:
            ret, frame = self.camera.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = tk.PhotoImage(data=cv2.imencode('.png', frame)[1].tobytes())
                self.label.config(image=self.photo)
        else:
            self.label.config(image=None)

        self.root.after(10, self.update)

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()
