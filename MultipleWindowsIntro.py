import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

class Extra(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("This is some bullshit")
        self.geometry("400x300")
        ttk.Label(self, text="Bullshit label 1").pack(expand=True)
        ttk.Label(self, text="Bullshit label 2").pack(expand=True)
        ttk.Button(self, text="Bullshit Button 1").pack(expand=True)


def ask_yes_no():
    #answer = messagebox.askquestion("Title", "Do u like coffe?")
    #print(answer)
    messagebox.askyesno("Some Information Title", "Your Hair is messy")
    
def create_window():
    global extra_window
    extra_window = Extra()
    #extra_window.title("This is some bullshit")
    #extra_window.geometry("400x300")
    #label1 = ttk.Label(extra_window, text="Bullshit label 1").pack(expand=True)
    #label2 = ttk.Label(extra_window, text="Bullshit label 2").pack(expand=True)
    #button1 = ttk.Button(extra_window, text="Bullshit Button 1").pack(expand=True)

def close_window():
    extra_window.destroy()

window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Multiple Windows")

                 
button1 = ttk.Button(window, text="open main window", command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text="destroy main window", command=close_window)
button2.pack(expand=True)

button3 = ttk.Button(window, text="yes or no question", command=ask_yes_no)
button3.pack(expand=True)

#run
window.mainloop()