import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Menu Intro")

#menu
menu1 = ttk.Menu(window)

#submenu
file_menu = ttk.Menu(menu1, tearoff=False) #tearOff doesnt do anything on macOS
file_menu.add_command(label="New", command=lambda: print("new File"))
file_menu.add_command(label="Open", command=lambda: print("Open File"))
file_menu.add_separator() #doesnt do anything on macOS
menu1.add_cascade(label="File", menu=file_menu)

#submenu2
help_menu = ttk.Menu(menu1, tearoff=False)
help_menu.add_command(label="Help Entry", command=lambda: print("help"))

help_check_stringvalue = ttk.StringVar()
help_menu.add_checkbutton(label="check", onvalue="on", offvalue="off", variable=help_check_stringvalue)

#submenu3 
edit_menu = ttk.Menu(menu1, tearoff=False)
submenu_of_edit_menu = ttk.Menu(edit_menu, tearoff=False)
edit_menu.add_cascade(label="submenuOfEditMenu", menu=submenu_of_edit_menu)
submenu_of_edit_menu.add_command(label="LOL", command=lambda: print("Edit"))
menu1.add_cascade(label="Edit", menu=edit_menu)

menu1.add_cascade(label="Help", menu=help_menu)

window.configure(menu=menu1)

#menu button
menu_button = ttk.Menubutton(window, text="Menu Button")
menu_button.pack()

button_sub_menu = ttk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="entry1", command=lambda: print("test 1"))
button_sub_menu.add_checkbutton(label="check1", command=lambda: print("check1"))
menu_button.configure(menu=button_sub_menu)

#run
window.mainloop()