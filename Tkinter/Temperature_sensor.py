import tkinter as tk
from tkinter import ttk

# create window
window = tk.Tk()
window.title("Temperature sensor -> Reading & Conversion")
window.geometry('500x400')

# title
title_label = ttk.Label(master=window, text='Celsius to Fahrenheit', font='arial 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='convert')
entry.pack(side='left',padx=10)
button.pack(side='left') # button inside de input_frame
input_frame.pack(pady=10)

# output
output_label = ttk.Label(master=window, text='Output',font='arial 24')
output_label.pack(pady=10)

window.mainloop() 