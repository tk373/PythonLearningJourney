import tkinter as tk
import ttkbootstrap as ttk

class App(ttk.Window):
    def __init__(self, start_size):

        #main setup
        super().__init__(themename="darkly")
        self.title("responsive Layout") #or just straight in the top funtion
        self.geometry(f"{start_size[0]}x{start_size[1]}")

        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill="both")

        
        #widgets
        

        #run
        self.mainloop()
