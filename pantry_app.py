#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, simpledialog
import pickle

class PantryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantry App")

        self.pantry_items = {}

        self.label = tk.Label(self.root, text="Pantry Items")
        self.label.pack(pady=20)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.remove_button = tk.Button(self.root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Items", command=self.save_items)
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load Items", command=self.load_items)
        self.load_button.pack(pady=10)

        self.edit_button = tk.Button(self.root, text="Edit Item", command=self.edit_item)
        self.edit_button.pack(pady=10)

        self.load_items()

    def add_item(self):
        item = simpledialog.askstring("Input", "Enter the pantry item name:")
        if item:
            qty = simpledialog.askinteger("Input", f"Enter quantity for {item}:")
            if qty:
                self.pantry_items[item] = qty
                self.update_listbox()

    def remove_item(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        item = self.listbox.get(selected[0]).split(" - ")[0]
        if item in self.pantry_items:
            del self.pantry_items[item]
            self.update_listbox()

    def save_items(self):
        with open("pantry_data.pkl", "wb") as file:
            pickle.dump(self.pantry_items, file)
        messagebox.showinfo("Info", "Pantry items saved!")

    def load_items(self):
        try:
            with open("pantry_data.pkl", "rb") as file:
                self.pantry_items = pickle.load(file)
            self.update_listbox()
        except FileNotFoundError:
            pass

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for item, qty in self.pantry_items.items():
            self.listbox.insert(tk.END, f"{item} - {qty}")

    def edit_item(self):
        selected = self.listbox.curselection()
        if not selected:
            return
        item = self.listbox.get(selected[0]).split(" - ")[0]

        new_item_name = simpledialog.askstring("Edit Item", f"Edit name of '{item}':", initialvalue=item)
        if new_item_name is None:  # if the user cancels the edit
            return

        new_item_qty = simpledialog.askinteger("Edit Quantity", f"Edit quantity for '{new_item_name}':", initialvalue=self.pantry_items[item])
        if new_item_qty is None:  # if the user cancels the edit
            return

        del self.pantry_items[item]  # remove old item
        self.pantry_items[new_item_name] = new_item_qty  # add updated item

        self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = PantryApp(root)
    root.mainloop()
