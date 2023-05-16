import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    outputString.set(km_output)

#window
window = ttk.Window(themename="darkly")
window.title("COnverter")
window.geometry("300x150")

#title
title_label = ttk.Label(master=window, text="Miles to Kilometers", font="Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
entry.pack(side="left", padx=5)
button.pack(side="left")
input_frame.pack(pady=10)

#output
outputString = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font="Calibri 24", textvariable=outputString)
output_label.pack()

#run
window.mainloop()