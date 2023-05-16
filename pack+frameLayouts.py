import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("Packet intro")
window.iconbitmap("Stark.ico")

#top frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text="First Label", background="red")
label2 = ttk.Label(top_frame, text="Second Label", background="blue")

#middle widget
label3 = ttk.Label(window, text="Another Label", background="green")

#bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text="Last Label", background="orange")
button1 = ttk.Button(bottom_frame, text="A Button")
button2 = ttk.Button(bottom_frame, text="Another Button")

#exercise frame
Last_Frame = ttk.Frame(bottom_frame)
button3 = ttk.Button(Last_Frame, text="button 3")
button4 = ttk.Button(Last_Frame, text="button 4")
button5 = ttk.Button(Last_Frame, text="button 5")

#top layout
label1.pack(side="left", fill="both", expand=True)
label2.pack(side="left", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)

#middle layout
label3.pack(expand=True)

#bottom layout
button1.pack(side="left", expand=True, fill="both")
label4.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")
bottom_frame.pack(expand=True, fill="both", padx=20, pady=20)

#exercise layout
button3.pack(expand=True, fill="both")
button4.pack(expand=True, fill="both")  
button5.pack(expand=True, fill="both")
Last_Frame.pack(side="left", expand=True, fill="both")

#run
window.mainloop()