import tkinter as tk
from tkinter import ttk

def convert():
    temp_input_celsius = entry_int.get()
    temp_output_farenheit = (temp_input_celsius*9/5) + 32
    output_string.set(temp_output_farenheit)

# create window
window = tk.Tk()
window.title("Temperature sensor -> Reading & Conversion")
window.geometry('500x400')

# title
title_label = ttk.Label(
    master=window,
    text='Celsius to Fahrenheit',
    font='arial 24 bold')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command= convert)
entry.pack(side='left',padx=10)
button.pack(side='left') # button inside de input_frame
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font='arial 24',
    textvariable=output_string)
output_label.pack(pady=10)

window.mainloop() 