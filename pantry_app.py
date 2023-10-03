#!/usr/bin/env python3

import tkinter as tk
from tkinter import simpledialog, messagebox

class PantryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantry App")

        # List to store pantry items
        self.pantry_items = []

        # Create UI Elements
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack(pady=10)

        self.listbox = tk.Listbox(root, width=50, height=20)
        self.listbox.pack(pady=20)

    def add_item(self):
        item = simpledialog.askstring("Add Item", "What item would you like to add?")
        if item:
            self.pantry_items.append(item)
            self.update_listbox()

    def remove_item(self):
        try:
            idx = self.listbox.curselection()
            if idx:
                del self.pantry_items[idx[0]]
                self.update_listbox()
            else:
                messagebox.showinfo("Info", "Please select an item to remove.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item in self.pantry_items:
            self.listbox.insert(tk.END, item)

if __name__ == "__main__":
    root = tk.Tk()
    app = PantryApp(root)
    root.mainloop()
