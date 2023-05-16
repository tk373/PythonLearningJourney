import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400+456+291")
window.title("Grid Layout")
window.iconbitmap("Stark.ico")

#main frame1
main_frame1 = ttk.Frame(window)

#main frame2
main_frame2 = ttk.Frame(window)

#layout main frame1
main_frame1.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame2.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

#menu widgets
menu_button1 = ttk.Button(main_frame1, text="Button 1")
menu_button2 = ttk.Button(main_frame1, text="Button 2")
menu_button3 = ttk.Button(main_frame1, text="Button 3")

menu_slider1 = ttk.Scale(main_frame1, orient="vertical")
menu_slider2 = ttk.Scale(main_frame1, orient="vertical")

toggle_frame= ttk.Frame(main_frame1)
menu_toggle1 = ttk.Checkbutton(toggle_frame, text="check 1")
menu_toggle2 = ttk.Checkbutton(toggle_frame, text="check 2")

entry = ttk.Entry(main_frame1)

#menu layout
main_frame1.columnconfigure((0,1,2), weight=1, uniform="a")
main_frame1.rowconfigure((0,1,2,3,4,5), weight=1, uniform="a")

menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2)
menu_button2.grid(row=0, column=2, sticky="nsew")
menu_button3.grid(row=1, column=0, columnspan=3, sticky="nsew")

menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

#toggle layout
toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
menu_toggle1.pack(side="left", expand=True)
menu_toggle2.pack(side="left", expand=True)

#entry layout
#entry.place(relx=0.5, rely=0.95, relwidth=0.9, relheight=0.05, anchor="center")
entry.grid(row=5, column=0, columnspan=3, sticky="new", padx=10)

# main widgets
entry_frame = ttk.Frame(main_frame2)
main_label1 = ttk.Label(entry_frame, text="label 1", background="blue")
main_button1 = ttk.Button(entry_frame, text="button 1")

entry_frame2 = ttk.Frame(main_frame2)
main_label2 = ttk.Label(entry_frame2, text="label 2", background="blue")
main_button2 = ttk.Button(entry_frame2, text="button 2")

#main layout
entry_frame.pack(side="left", expand=True, fill="both", padx=20, pady=20)
entry_frame2.pack(side="left", expand=True, fill="both", padx=20, pady=20)

main_label1.pack(expand=True, fill="both")
main_button1.pack(expand=True, fill="both", pady= 10)

main_label2.pack(expand=True, fill="both")
main_button2.pack(expand=True, fill="both", pady= 10)

#label1 = ttk.Label(entry_frame, background="red").pack(expand=True, fill="both")
#label2 = ttk.Label(entry_frame2, background="yellow").pack(expand=True, fill="both")


#run
window.mainloop()