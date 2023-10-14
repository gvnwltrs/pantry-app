#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button
import pickle

class AddOrEditDialog:
    def __init__(self, parent, item=None, qty=None):
        self.top = Toplevel(parent)
        self.top.title("Add or Edit Item")

        Label(self.top, text="Item Name:").pack(pady=10)
        self.name_entry = Entry(self.top)
        self.name_entry.pack(pady=5)
        if item:
            self.name_entry.insert(0, item)

        Label(self.top, text="Quantity:").pack(pady=10)
        self.qty_entry = Entry(self.top)
        self.qty_entry.pack(pady=5)
        if qty:
            self.qty_entry.insert(0, str(qty))

        Button(self.top, text="Submit", command=self.submit).pack(pady=20)

        self.result = None

    def submit(self):
        item_name = self.name_entry.get().strip()
        try:
            item_qty = int(self.qty_entry.get().strip())
            if item_name:
                self.result = (item_name, item_qty)
                self.top.destroy()
            else:
                messagebox.showerror("Error", "Item name cannot be empty.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid quantity.")

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
        
        self.edit_button = tk.Button(self.root, text="Edit Item", command=self.edit_item)
        self.edit_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Save Items", command=self.save_items)
        self.save_button.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load Items", command=self.load_items)
        self.load_button.pack(pady=10)


        self.load_items()

    def add_or_edit_item(self, item=None, qty=None):
        dialog = AddOrEditDialog(self.root, item, qty)
        self.root.wait_window(dialog.top)
        return dialog.result

    def add_item(self):
        result = self.add_or_edit_item()
        if result:
            item_name, item_qty = result
            self.pantry_items[item_name] = item_qty
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
        qty = self.pantry_items[item]

        result = self.add_or_edit_item(item, qty)
        if result:
            new_item_name, new_item_qty = result

            if new_item_name != item:
                del self.pantry_items[item] 

            self.pantry_items[new_item_name] = new_item_qty
            self.update_listbox()
 
    

  

if __name__ == "__main__":
    root = tk.Tk()
    app = PantryApp(root)
    root.mainloop()
