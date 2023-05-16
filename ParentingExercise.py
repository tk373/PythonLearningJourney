import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Frames and Parenting")

#frame 
frame = ttk.Frame(master=window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side="left")

#master setting
label = ttk.Label(master=frame, text="Label in frame")
label.pack()

button = ttk.Button(master=frame, text="button in frame")
button.pack()

#example 
label2 = ttk.Label(master=window, text="Label outside of frame")
label2.pack(side="left")

#exercise
#frame2
frame2 = ttk.Frame(master=window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame2.pack_propagate(False)
frame2.pack(side="left")

button = ttk.Button(master=frame2, text="button in frame")
button.pack()

entry = ttk.Entry(master=frame2)
entry.pack()

#example 
label2 = ttk.Label(master=frame2, text="Label outside of frame")
label2.pack()


#run 
window.mainloop()