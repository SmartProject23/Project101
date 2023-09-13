import tkinter as tk
import subprocess

def Register():
    script_1 = 'add_images.py'
    subprocess.run(['python', script_1])

def Start_System():
    script_2 = 'main.py'
    subprocess.run(['python', script_2])

def Start_droid():
    script_3 = 'droid.py'
    subprocess.run(['python', script_3])

def Start_external():
    script_4 = 'external.py'
    subprocess.run(['python', script_4])

def open_csv_in_excel():
    csv_file_name = 'Report.csv'
    subprocess.run(['start', csv_file_name], shell=True)

# def Start_System():
#     script_6 = 'main.py'
#     subprocess.run(['python', script_6])
    
# def Start_System():
#     script_7 = 'main.py'
#     subprocess.run(['python', script_7])

# Create the main window
root = tk.Tk()
root.title("Welcome to Smart_Technology Monitoring_System")

# Function to quit the application
def quit_app():
    root.quit()

# Create buttons with padding and background colors
button_Register = tk.Button(root, text="Register New", command=Register, padx=100, pady=10, bg="green")
button_Start_System = tk.Button(root, text="Start System", command=Start_System, padx=100, pady=10, bg="blue")
button_Start_droid = tk.Button(root, text="  Start droid  ", command=Start_droid, padx=100, pady=10, bg="green")
button_Start_USBCam = tk.Button(root, text="Start USBCam", command=Start_external, padx=100, pady=10, bg="blue")
button_Opencsv = tk.Button(root, text="Open_Report", command=open_csv_in_excel, padx=100, pady=10, bg="brown")
# button_Start_System = tk.Button(root, text="Start System", command=Start_System, padx=80, pady=10, bg="blue")


button_quit = tk.Button(root, text="      Quit      ", command=quit_app, padx=100, pady=10, bg="red")

# Pack buttons
button_Register.pack(padx=80, pady=10)
button_Start_System.pack(padx=80, pady=10)
button_Start_droid.pack(padx=80, pady=10)
button_Start_USBCam.pack(padx=80, pady=10)
button_Opencsv.pack(padx=80, pady=10)
button_quit.pack(padx=80, pady=10)
root.mainloop()
