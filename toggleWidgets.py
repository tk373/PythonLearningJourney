import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("Grid Layout")
window.iconbitmap("Stark.ico")

#place 
# def toggle_label_place():
#     global label_visibility
# 
#     if label_visibility: 
#         label1.place_forget()
#         label_visibility = False
#     else:
#         label_visibility = True
#         label1.place(relx=0.5, rely=0.5, anchor="center")
# 
# #place 
# button1 = ttk.Button(window, text="toggle label", command= toggle_label_place)
# button1.place(x=10, y=10)
# 
# label_visibility = True
# label1 = ttk.Label(window, text="a label")
# label1.place(relx=0.5, rely=0.5, anchor="center")

# grid 
#def toggle_enable_grid():
#    global label_visible
#
#    if label_visible:
#        label1.grid_forget()
#        label_visible = False
#    else:
#        label_visible = True
#        label1.grid(column=1, row=0)
#
#window.columnconfigure((0,1), weight=1, uniform="a")
#window.rowconfigure(0, weight=1, uniform="a")
#
#button1 = ttk.Button(window, text="toggle Label", command=toggle_enable_grid)
#button1.grid(column=0, row=0)
#
#label_visible = True
#label1 = ttk.Label(window, text="a label")
#label1.grid(column=1, row=0)

#pack
def toggle_label_pack():
    global label_visible

    if label_visible: 
        label1.pack_forget()
        label_visible = False
        frame.pack(expand=True, before=button1)
    else:
        frame.pack_forget()
        label1.pack(expand=True, before=button1)
        label_visible = True
        

label_visible = True
label1 = ttk.Label(window, text="a label")
label1.pack(expand=True)

button1 = ttk.Button(window, text="toggle Label", command=toggle_label_pack)
button1.pack()

frame = ttk.Frame(window)

#run
window.mainloop()