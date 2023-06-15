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

        sizeNotifier(self, {300: self.create_small_layout, 600: self.create_medium_layout, 1200: self.create_big_layout})

        #run
        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill="both")

        ttk.Label(self.frame, text="Label 1", background="red").pack(expand=True, fill="both", padx=10, pady=5)
        ttk.Label(self.frame, text="Label 2", background="green").pack(expand=True, fill="both", padx=10, pady=5)
        ttk.Label(self.frame, text="Label 3", background="blue").pack(expand=True, fill="both", padx=10, pady=5)
        ttk.Label(self.frame, text="Label 4", background="yellow").pack(expand=True, fill="both", padx=10, pady=5)

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight=1, uniform="a")
        self.frame.rowconfigure((0,1), weight=1, uniform="a")
        self.frame.pack(expand=True, fill="both")

        ttk.Label(self.frame, text="Label 1", background="red").grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 2", background="green").grid(column=1, row=0, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 3", background="blue").grid(column=0, row=1, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 4", background="yellow").grid(column=1, row=1, sticky="nsew", padx=10, pady=10)
    
    def create_big_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight=1, uniform="a")
        self.frame.rowconfigure((0,1,2), weight=1, uniform="a")
        self.frame.pack(expand=True, fill="both")

        ttk.Label(self.frame, text="Label 1", background="red").grid(column=0, row=0, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 2", background="green").grid(column=1, row=0, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 3", background="blue").grid(column=0, row=1, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 4", background="yellow").grid(column=1, row=1, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 4", background="red").grid(column=0, row=2, sticky="nsew", padx=10, pady=10)
        ttk.Label(self.frame, text="Label 4", background="green").grid(column=1, row=2, sticky="nsew", padx=10, pady=10)

class sizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window
        self.size_dict = {key: value for key, value in size_dict.items()}
        self.current_min_size = None
        self.window.bind("<Configure>", self.check_size)

        self.window.update()

        min_height = self.window.winfo_height()
        min_width = list(self.size_dict)[0]
        self.window.minsize(min_width, min_height)

        
    
    def check_size(self, event):
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

            for min_size in self.size_dict:
                delta = window_width - min_size
                if delta >= 0:
                    checked_size = min_size

            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]() 

app = App((400,300))
