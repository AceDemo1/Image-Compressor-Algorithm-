#!/usr/bin/python3
import os
from PIL import Image
import subprocess

# Check if a display is available (for GUI environments)
def is_gui_env():
    return os.getenv('DISPLAY') is not None

# Function to select file in GUI environment using Tkinter
def get_file_path_gui():
    from tkinter.filedialog import askopenfilename, asksaveasfilename
    file_path = askopenfilename()
    if not file_path:
        print("No file selected.")
        return None, None
    save_path = asksaveasfilename(defaultextension=".JPG")
    if not save_path:
        print("No save location selected.")
        return None, None
    return file_path, save_path

# Function to select file in non-GUI environment using Zenity
def get_file_path_non_gui():
    try:
        # Select input file
        input_file = subprocess.check_output(['zenity', '--file-selection']).decode('utf-8').strip()
        if not input_file:
            print("No file selected.")
            return None, None
        # Select output save path
        save_path = subprocess.check_output(['zenity', '--file-selection', '--save']).decode('utf-8').strip()
        if not save_path:
            print("No save location selected.")
            return None, None
        return input_file, save_path
    except subprocess.CalledProcessError:
        print("Zenity operation was canceled.")
        return None, None

# Main function to compress image
def compress_image(input_path, output_path):
    img = Image.open(input_path)
    height, width = img.size
    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(output_path + '_compressed.JPG')

# Detect environment and get file paths
if is_gui_env():
    file_path, save_path = get_file_path_gui()
else:
    file_path, save_path = get_file_path_non_gui()

# Proceed only if valid paths were selected
if file_path and save_path:
    compress_image(file_path, save_path)
    print(f"Image successfully compressed and saved to: {save_path}_compressed.JPG")
else:
    print("Operation aborted.")

