import tkinter as tk

class App(tk.Frame):
    def __init__(self, data, master=None):
        super().__init__(master)
        self.master = master
        self.data = data
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.t = Table(self.master, self.data)
        
class Table:
    def __init__(self, master, data):
        self.data = data
        self.table = tk.Listbox(master, height=10, width=15, 
                                bg='white', fg='black', 
                                font=('Consolas', 30, 'bold'),
                                justify='left')

        for i in range(len(data)):
            self.table.insert(i + 1, f"{data[i][0]} - {data[i][1]}")
        
        self.table.pack(side='top')