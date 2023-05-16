import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("Grid Layout")
window.iconbitmap("Stark.ico")

#widgets 
label1 = ttk.Label(window, text="label 1", background="red")
label2 = ttk.Label(window, text="label 2", background="blue")
label3 = ttk.Label(window, text="label 3", background="green")
label4 = ttk.Label(window, text="label 4", background="yellow")
button1 = ttk.Button(window, text="button 1")
button2 = ttk.Button(window, text="button 2")
entry = ttk.Entry(window)

#grid definition
window.columnconfigure((0,1,2), weight=1, uniform="a")
window.columnconfigure(3, weight=10, uniform="a")
window.rowconfigure((0,1,2), weight=1, uniform="a")
window.rowconfigure(3, weight=3, uniform="a")

#place a widget
label1.grid(row=0, column=0, sticky="nsew")
label2.grid(row=1, column=1, rowspan=2, columnspan=2, sticky="nsew")
label3.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
label4.grid(row=3, column=3, sticky="se")

#run
window.mainloop()