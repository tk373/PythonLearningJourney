import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.title("Combo and Spin")
window.geometry("600x400")

#comboboc
items = ("Ice cream", "pizza", "broccoli")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(master=window, textvariable=food_string)
combo.configure(values = items)
combo.pack()

#events for combobox
combo.bind("<<ComboboxSelected>>", lambda event: combo_label.config(text=f"selected value: {food_string.get()}"))

combo_label = ttk.Label(master=window, text="a label")
combo_label.pack()

#spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(master=window, from_ = 3, to = 20, command=lambda: print(spin_int.get()),textvariable=spin_int)
spin.bind("<<Increment>>", lambda event: print("up"))
spin.bind("<<Decrement>>", lambda event: print("down"))
spin.pack()

#spinbox exercise
items_spinbox = ("A", "B", "C", "D", "E")
spingbox_string = tk.StringVar(value=items_spinbox[0])
spin2 = ttk.Spinbox(master=window, textvariable=spingbox_string)
spin2.configure(values=items_spinbox)
spin2.bind("<<Decrement>>", lambda event: print(spingbox_string.get()))
spin2.pack()


#run 
window.mainloop()