import tkinter as tk
from tkinter import ttk

class SimpleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.create_widgets()

    def create_widgets(self):
        self.name_label = ttk.Label(self, text="Name:")
        self.name_label.grid(row=0, column=0)

        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=1)

        self.age_label = ttk.Label(self, text="Age:")
        self.age_label.grid(row=1, column=0)

        self.age_entry = ttk.Entry(self)
        self.age_entry.grid(row=1, column=1)

        self.save_button = ttk.Button(self, text="Save", command=self.save_data)
        self.save_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.data_tree = ttk.Treeview(self)
        self.data_tree["columns"] = ("name", "age")
        self.data_tree.column("#0", width=50, minwidth=50, stretch=tk.NO)
        self.data_tree.column("name", width=150, minwidth=150, stretch=tk.NO)
        self.data_tree.column("age", width=50, minwidth=50, stretch=tk.NO)
        self.data_tree.heading("#0", text="ID", anchor=tk.W)
        self.data_tree.heading("name", text="Name", anchor=tk.W)
        self.data_tree.heading("age", text="Age", anchor=tk.W)
        self.data_tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def save_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        if name and age:
            id = self.data_tree.insert("", "end", text=str(len(self.data_tree.get_children()) + 1), values=(name, age))
            self.name_entry.delete(0, "end")
            self.age_entry.delete(0, "end")


if __name__ == "__main__":
    app = SimpleApp()
    app.mainloop()
