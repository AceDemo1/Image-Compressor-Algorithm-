#!/usr/bin/python3
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_path = askopenfilename()

img =Image.open(file_path)
height, width = img.size
img = img.resize((width, height), Image.ANTIALIAS)
save_path = asksavefilename()

img.save(save_path + '_compressed.JPG')
