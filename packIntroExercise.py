import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("Packet intro")
window.iconbitmap("Stark.ico")

#widgets
label1 = ttk.Label(window, text="First Label", background="red")
label2 = ttk.Label(window, text="Second Label", background="blue")
label3 = ttk.Label(window, text="Last Label", background="green")
button = ttk.Button(window, text="Button")

#layout
label1.pack(side="top", fill="both", padx=20,pady=20)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")

#run
window.mainloop()