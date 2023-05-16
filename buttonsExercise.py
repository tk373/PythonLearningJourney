import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="darkly")
window.title("Buttons")
window.geometry("600x400")

def button_func():
    print("preseed")
    print(radiot_var.get())

button_string = tk.StringVar(value="A button with string var")
button1 = ttk.Button(window, text="a simple button", command=button_func, textvariable=button_string)
button1.pack()

check_var = tk.IntVar()
check = ttk.Checkbutton(master=window, text="checkbox 1", command=lambda: print(check_var.get()), variable=check_var, onvalue=10, offvalue=5)
check.pack()

check2 = ttk.Checkbutton(master=window, text="Checkbox2", command=lambda: check_var.set(5))
check2.pack()

radiot_var = tk.StringVar()
radio1 = ttk.Radiobutton(master=window, text="Radiobutton1", value="radio1", command=lambda: print(radiot_var.get()), variable=radiot_var)
radio2 = ttk.Radiobutton(master=window, text="Radiobutton2", value=2, variable=radiot_var)
radio1.pack()
radio2.pack()

window.mainloop()
