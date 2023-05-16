import tkinter as tk
import ttkbootstrap as ttk
import random

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Table")

#data
first_names = ["bob", "maria", "alex", "fabian", "silvan", "anes", "fabio", "lisa"]
last_names = ["smith", "brown", "wilson", "strich", "hegner", "ganic", "cangini", "kistler"]

#treeview
table = ttk.Treeview(master=window, columns=("first", "last", "email"), show="headings")
table.heading("first", text="first name")
table.heading("last", text="last name")
table.heading("email", text="email")
table.pack(fill="both", expand=True)

#insert data into table
# table.insert(parent="", index=0, values=("John", "Doe", "JohnDoe@gmail.com"))
for i in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = f"{first[0]}{last}@email.com"
    data = (first, last, email)
    table.insert(parent="", index=0, values=data)

table.insert(parent="", index=tk.END, values=("XXXX", "CCCCC", "BBBB"))

#events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])

def delete_items(_):
    print("delete")
    for i in table.selection():
        table.delete(i)

table.bind("<<TreeviewSelect>>", item_select)
table.bind("<Delete>", delete_items)

#run
window.mainloop()