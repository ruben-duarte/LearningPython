from PIL import Image, ImageFilter
import tkinter as tk

img = Image.open('./images/engine.jpg')
print(img.format)
print(img.size)
print(img.mode)