import tkinter as tk
import ttkbootstrap as ttk

def create_segement(master, label_text, button_text):
    frame = ttk.Frame(master=master)
    
    #grid 
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0,1,2), weight=1, uniform="a")

    #widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    return frame

class Segment(ttk.Frame):
    def __init__(self, master, label_text, button_text, exercise_box_button_text):
        super().__init__(master)

        #grid 
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform="a")
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.create_exercise_box(exercise_box_button_text).grid(row=0, column=2, sticky="nsew", pady=10)

        #placement
        self.pack(expand=True, fill="both")
    
    def create_exercise_box(self, button_text):
        frame1 = ttk.Frame(master=self)

        ttk.Entry(frame1).pack(expand=True, fill="both")
        ttk.Button(frame1, text=button_text).pack(expand=True, fill="both")

        return frame1



#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("widgets and return")
window.iconbitmap("Stark.ico")

#widgets 
#create_segement(window, "label1", "button1").pack(expand=True, fill="both")

Segment(window, "label1", "button1", "button0")
Segment(window, "label2", "button2", "button1")
Segment(window, "label3", "button3", "button2")
Segment(window, "label3", "button3", "button3")
Segment(window, "label3", "button3", "button4")
Segment(window, "label3", "button3", "button5")

#run
window.mainloop()