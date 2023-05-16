import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("More on the window")
window.iconbitmap("Stark.ico")

#widgets
label1 = ttk.Label(window, text="Label1", background="red")
label2 = ttk.Label(window, text="Label2", background="blue")

#pack
#label1.pack(side="left", expand=True, fill="both")
#label2.pack(side="left", expand=True, fill="both")

#grid
#window.columnconfigure(0, weight=1)
#window.columnconfigure(1, weight=1)
#window.columnconfigure(2, weight=2)
#window.rowconfigure(0, weight=1)
#window.rowconfigure(1, weight=1)
#
#label1.grid(row=0, column=1, sticky="nsew")
#label2.grid(row=1, column=1, columnspan=2, sticky="nsew")

#place 
label1.place(x=100, y=200, width=200, height=100)
label2.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="sw")


#run 
window.mainloop()