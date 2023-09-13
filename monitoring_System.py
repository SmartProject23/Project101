import tkinter as tk
import subprocess
import sys

def run_script(script_name):
    try:
        subprocess.run(['python', script_name])
    except Exception as e:
        print(f"Error running {script_name}: {e}")

def quit_application():
    root.quit()
    sys.exit()
def open_csv_in_excel():
    csv_file_name = 'Report.csv'
    subprocess.run(['start', csv_file_name], shell=True)

root = tk.Tk()
root.title("Smart_Technologies_Monitoring_System")
root.configure(bg="#00008B")

title_label = tk.Label(root, text="SMART_TECH_MONITORING_SYSTEM", font=("Helvetica", 20, "bold"), fg="white", bg="#00008B")
title_label.grid(row=0, column=0, columnspan=3, pady=(10, 5))


dpi = 96
width_inches = 1
height_inches = 1
width_pixels = int(width_inches * dpi)
height_pixels = int(height_inches * dpi)

button_style = {
    "width": width_pixels,
    "height": height_pixels,
    "padx": 90,
    "pady": 60,
    "cursor": "hand2",  
    "relief": tk.RAISED,  
    "borderwidth": 3,    
}

scripts = [
    {"name": "Script 1", "script": "add_images.py", "resources": "resources/add.png"},
    {"name": "Script 2", "script": "external.py", "resources": "resources/webcam.png"},
    {"name": "Script 3", "script": "script3.py", "resources": "resources/reports.png"},
    {"name": "Script 4", "script": "droid.py", "resources": "resources/droid.png"},
    {"name": "Script 5", "script": "main.py", "resources": "resources/systemcam.png"},
    {"name": "Script 6", "script": " ", "resources": "resources/quit.png"}
]

buttons = []
for i, script_info in enumerate(scripts):
    script_name = script_info["script"]
    resources = script_info["resources"]

    image = tk.PhotoImage(file=resources)

    button = tk.Button(root, image=image, text=script_info["name"], compound="top", command=lambda name=script_name: run_script(name))
    button.image = image
    button.config(**button_style)
    buttons.append(button)

    if i == len(scripts) - 1:
        button.config(command=quit_application)

    if i == len(scripts) - 4:
        button.config(command=open_csv_in_excel)

for i, button in enumerate(buttons):
    row_num = i // 3 + 1 
    col_num = i % 3
    button.grid(row=row_num, column=col_num, padx=10, pady=10)

root.mainloop()
