#!/usr/bin/python
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()

img = PIL.Image.open(file_path)
height, width = img.size
img = im.resize((height, width) PIL.Image.ANTIALIAS)
save_path = asksavefilename()

image.save(save_path + '_compressed.JPG')
