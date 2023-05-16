import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
#window.geometry("600x400+456+291")
window.title("More on the window")
window.iconbitmap("Stark.ico")

#start window in the middle of the screen
window_width = 600
window_height = 400
display_width = window.winfo_screenmmwidth()
display_height = window.winfo_screenheight()

left = int((display_width - window_width) / 2)
top = int((display_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{left}+{top}")

#windos attributes
#window.minsize(200,100)
# window.maxsize(800,700)
#window.resizable(True, False) #allows you to only saize the window in either the x or y direction

#screen attributes
#print(window.winfo_screenwidth())
#print(window.winfo_screenheight())

#window attributes
#window.attributes("-alpha", 1)
#window.attributes("-topmost", True) # sets window on top of everything

#security event
window.bind("<Escape>", lambda event: window.quit())
#window.attributes("-fullscreen", True) #only works if no max-size is enabled
#window.attributes("-disable", True) doesnt let u execute the app if this is added because of the safety risks

#title bar
#window.overrideredirect(True)
#grip = ttk.Sizegrip(window)
#grip.place(relx=1.0, rely=1.0, anchor="se")

#run 
window.mainloop()