import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Tab widget")

#notebook widget
notebook = ttk.Notebook(master=window)

#tab1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="Text in Tab1")
button1 = ttk.Button(tab1, text="Button in Tab1")
label1.pack()
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="Label in Tab2")
entry2 = ttk.Entry(tab2)
label2.pack()
entry2.pack()

tab3 = ttk.Frame(notebook)
Label3 = ttk.Label(tab3, text="Label in Tab3")
button3 = ttk.Button(tab3, text="Button in Tab 3")
button4 = ttk.Button(tab3, text="Second Button in Tab 3")
tab3.pack()
button3.pack()
button4.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")
notebook.pack()

#run
window.mainloop()