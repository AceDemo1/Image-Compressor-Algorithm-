#!/usr/bin/python3
import os
from PIL import Image

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

# Function to select file in non-GUI environment using manual input
def get_file_path_non_gui():
    # Manually ask for input file path
    input_file = input("Enter the path to the input image file: ").strip()
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return None, None

    # Manually ask for save path
    save_path = input("Enter the path where the compressed image should be saved: ").strip()
    return input_file, save_path
def ask_image_format():
    while True:
        choice = input("Do you want to save the image in PNG or JPEG format?").islower()
        if choice in ['png', 'jpeg']:
            return choice
        else:
            print("Invalid choice. Please enter 'png' or 'jpeg'.")

# Function to get desired compression percentage
def get_compression_percentage():
    while True:
        try:
            percentage = int(input("Enter the desired compression percentage (1-100): "))
            if 1 <= percentage <= 100:
                return percentage
            else:
                print("Please enter a value between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value between 1 and 100.")

# Main function to compress image
def compress_image(input_path, output_path, image_format, quality=None):
    try:
        img = Image.open(input_path)
        if image_format == 'jpeg':
            img.save(output_path + '.jpg', quality=quality)
        else:
            img.save(output_path + ".png")
    except Exception as e: 
        print(f"Error compressing image: {e}")

# Detect environment and get file paths
if is_gui_env():
    file_path, save_path = get_file_path_gui()
else:
    file_path, save_path = get_file_path_non_gui()

# Proceed only if valid paths were selected
if file_path and save_path:
    image_format = ask_image_format()

    # If JPEG is selected, compress the image with the user-provided quality percentage
    if image_format == 'jpeg':
        compression_percentage = get_compression_percentage()
        compress_image(file_path, save_path, image_format, quality=compression_percentage)
    else:
        compress_image(file_path, save_path, image_format)
    print(f"Image successfully compressed and saved to: {save_path}_compressed.JPG")
else:
    print("Operation aborted.")

