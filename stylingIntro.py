import tkinter as tk
import ttkbootstrap as ttk
from tkinter import font

#window
window = ttk.Window(themename="darkly")
window.geometry("400x300")
window.title("Styling")

#style
style = ttk.Style()
#print(style.theme_names())
style.configure("new.TButton", background="green")
style.map("new.TButton", foreground=[("pressed", "red"),("disabled", "yellow")], background=[("pressed", "blue"),("disabled", "green")])
style.configure("TFrame", background="pink")

frame = ttk.Frame(window, width=50, height=100)
frame.pack()
#print(font.families())

#widgets
label1 = ttk.Label(window, text="Label 1\nLmao this is funny", background="green", foreground="black", font=('Helvetica', 20), justify="center")
label1.pack(expand=True)

button1 = ttk.Button(window, text="Button 1", style='new.TButton')
button1.pack(expand=True)

#run 
window.mainloop()