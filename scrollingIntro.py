import tkinter as tk
import ttkbootstrap as ttk
from random import randint, choice

#setup 
window = ttk.Window()
window.geometry("600x400")
window.title("Scrolling")

#canvas
canvas = ttk.Canvas(window, bg="white", scrollregion=(0,0,1000,5000))
canvas.create_line(0,0,2000,5000, fill="green", width=10)
for i in range(100):
    l = randint(0,2000)
    t = randint(0,5000)
    r = l + randint(10,500)
    b= t + randint(10,500)
    color = choice(("red", "green", "blue", "yellow", "orange"))
    canvas.create_rectangle(l,t,r,b, fill=color)
canvas.pack(expand=True, fill="both")

#mouseWheel scrolling
canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-int(event.delta / 60), "units"))

#scrollbar
scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollbar2 = ttk.Scrollbar(window, orient="horizontal", command=canvas.xview)
canvas.configure(yscrollcommand = scrollbar.set)
canvas.configure(xscrollcommand= scrollbar2.set)
scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
scrollbar2.place(relx=0, rely=1, relwidth=1, anchor="sw")


#run
window.mainloop()  