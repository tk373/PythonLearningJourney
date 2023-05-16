import tkinter as tk
import ttkbootstrap as ttk
from tkinter import scrolledtext



#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Sliders")

#slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(master=window, command=lambda value: print(value), from_=0, to=25, length=300, orient="horizontal", variable=scale_float)
scale.pack()

#progressbar
progress = ttk.Progressbar(master=window, variable=scale_float, maximum=25)
progress.pack()

scrolled_text = scrolledtext.ScrolledText(master=window)
scrolled_text.pack()

#run
window.mainloop()