import tkinter as tk
import ttkbootstrap as ttk

def button_function():
    print("Pressed")

#create a window
window = ttk.Window(themename="darkly")
window.title("Windows and Widgets")
window.geometry("800x500")

#ttk widgets
label = ttk.Label(master=window, text="This Is a editor")
label.pack()

#create Widgets
text_input = tk.Text(master=window)
text_input.pack()

#ttk entry
entry = ttk.Entry(master=window)
entry.pack()

#button
button = ttk.Button(master=window, text="A button", command=button_function)
button.pack()

#run
window.mainloop()