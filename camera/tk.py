import tkinter as tk
import cv2
from tkinter import ttk

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")

        # Create a label to display the camera feed
        self.label = ttk.Label(root)
        self.label.pack()

        # Create a button to toggle the camera and a close button
        self.toggle_button = ttk.Button(root, text="Toggle Camera", command=self.toggle_camera)
        self.close_button = ttk.Button(root, text="Close", command=self.close_camera)

        self.toggle_button.pack()
        self.close_button.pack()

        self.is_camera_active = False
        self.camera = cv2.VideoCapture(0)  # Open the default camera (0)

        self.update()

    def toggle_camera(self):
        self.is_camera_active = not self.is_camera_active

    def close_camera(self):
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
