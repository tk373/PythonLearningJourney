import tkinter as tk
import ttkbootstrap as ttk

#window 
window = ttk.Window(themename="darkly")
window.geometry("600x400")
window.title("Canvas")

#canvas
canvas = tk.Canvas(master=window)
canvas.pack()

# anvas.create_rectangle((50, 50, 100, 200), fill="red", width=10, outline="green")
# anvas.create_line((0, 0, 100, 150), fill="green")
# anvas.create_oval((0, 0, 100, 100), fill="blue")
# anvas.create_polygon((0, 0, 100, 200, 300, 50), fill="gray")

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2), fill="white")

def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -=4
    brush_size = max(0,min(brush_size, 20))

brush_size = 4
canvas.bind("<Motion>", draw_on_canvas)
canvas.bind("<MouseWheel>", brush_size_adjust)

#run 
window.mainloop()