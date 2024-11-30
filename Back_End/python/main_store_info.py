import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

data_file = 'grocery_data.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {"items": []}

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    expiry_date = entry_expiry.get()
    location = entry_location.get()

    if not name or not quantity or not expiry_date:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Validate the expiry_date format
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Please enter a valid date in the format YYYY-MM-DD.")
        return

    new_item = {
        "name": name,
        "quantity": int(quantity),
        "expiry_date": expiry_date,
        "location": location,
    }
    data["items"].append(new_item)
    save_data()
    update_treeview()
    clear_entries()

def edit_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return
    
    index = int(tree.item(selected_item)["text"])
    data["items"][index] = {
        "name": entry_name.get(),
        "quantity": int(entry_quantity.get()),
        "expiry_date": entry_expiry.get(),
        "location": entry_location.get(),
    }
    save_data()
    update_treeview()
    clear_entries()

def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return
    
    index = int(tree.item(selected_item)["text"])
    del data["items"][index]
    save_data()
    update_treeview()
    clear_entries()

def group_items():
    grouped_data = {}
    for item in data["items"]:
        name = item["name"]
        quantity = item["quantity"]
        expiry_date = datetime.strptime(item["expiry_date"], "%Y-%m-%d")

        if name not in grouped_data:
            grouped_data[name] = {
                "total_quantity": 0,
                "expiry_dates": [],
                "locations": []
            }

        grouped_data[name]["total_quantity"] += quantity
        grouped_data[name]["expiry_dates"].append(expiry_date)
        grouped_data[name]["locations"].append(item["location"])

    grouped_items = []
    for name, details in grouped_data.items():
        # Calculate the average expiry date in timestamps
        avg_timestamp = sum(dt.timestamp() for dt in details["expiry_dates"]) / len(details["expiry_dates"])
        avg_expiry_date = datetime.fromtimestamp(avg_timestamp)
        
        grouped_items.append({
            "name": name,
            "quantity": details["total_quantity"],
            "avg_expiry": avg_expiry_date.strftime("%Y-%m-%d"),
            "locations": details["locations"]
        })
    return grouped_items

def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    for index, item in enumerate(group_items()):
        tree.insert('', 'end', text=index, values=(item["name"], item["quantity"], item["avg_expiry"]))

def show_item_details(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    index = int(tree.item(selected_item)["text"])
    item = group_items()[index]
    
    details = "\n".join([f"- Location: {loc}" for loc in set(item["locations"])])
    messagebox.showinfo("Item Details", f"Name: {item['name']}\nTotal Quantity: {item['quantity']}\n"
                                        f"Average Expiry Date: {item['avg_expiry']}\nLocations:\n{details}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)
    entry_location.delete(0, tk.END)

# Main Application
root = tk.Tk()
root.title("Grocery List Manager")
root.geometry("600x400")

# Treeview for displaying grouped items
tree = ttk.Treeview(root, columns=("Name", "Quantity", "Avg Expiry Date"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Avg Expiry Date", text="Average Expiry Date")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Button-3>", show_item_details)

# Entry widgets for new items
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(frame)
entry_quantity.grid(row=1, column=1)

tk.Label(frame, text="Expiry Date (YYYY-MM-DD)").grid(row=2, column=0)
entry_expiry = tk.Entry(frame)
entry_expiry.grid(row=2, column=1)

tk.Label(frame, text="Location").grid(row=3, column=0)
entry_location = tk.Entry(frame)
entry_location.grid(row=3, column=1)

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit Item", command=edit_item).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Item", command=delete_item).grid(row=0, column=2, padx=5)

# Populate treeview with grouped data
update_treeview()

root.mainloop()

data_file = 'grocery_data.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {"items": []}

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    expiry_date = entry_expiry.get()
    location = entry_location.get()

    if not name or not quantity or not expiry_date:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Validate the expiry_date format
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Please enter a valid date in the format YYYY-MM-DD.")
        return

    new_item = {
        "name": name,
        "quantity": int(quantity),
        "expiry_date": expiry_date,
        "location": location,
    }
    data["items"].append(new_item)
    save_data()
    update_treeview()
    clear_entries()

def edit_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return
    
    index = int(tree.item(selected_item)["text"])
    data["items"][index] = {
        "name": entry_name.get(),
        "quantity": int(entry_quantity.get()),
        "expiry_date": entry_expiry.get(),
        "location": entry_location.get(),
    }
    save_data()
    update_treeview()
    clear_entries()

def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return
    
    index = int(tree.item(selected_item)["text"])
    del data["items"][index]
    save_data()
    update_treeview()
    clear_entries()

def group_items():
    grouped_data = {}
    for item in data["items"]:
        name = item["name"]
        quantity = item["quantity"]
        expiry_date = datetime.strptime(item["expiry_date"], "%Y-%m-%d")

        if name not in grouped_data:
            grouped_data[name] = {
                "total_quantity": 0,
                "expiry_dates": [],
                "locations": []
            }

        grouped_data[name]["total_quantity"] += quantity
        grouped_data[name]["expiry_dates"].append(expiry_date)
        grouped_data[name]["locations"].append(item["location"])

    grouped_items = []
    for name, details in grouped_data.items():
        # Calculate the average expiry date in timestamps
        avg_timestamp = sum(dt.timestamp() for dt in details["expiry_dates"]) / len(details["expiry_dates"])
        avg_expiry_date = datetime.fromtimestamp(avg_timestamp)
        
        grouped_items.append({
            "name": name,
            "quantity": details["total_quantity"],
            "avg_expiry": avg_expiry_date.strftime("%Y-%m-%d"),
            "locations": details["locations"]
        })
    return grouped_items

def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    for index, item in enumerate(group_items()):
        tree.insert('', 'end', text=index, values=(item["name"], item["quantity"], item["avg_expiry"]))

def show_item_details(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    index = int(tree.item(selected_item)["text"])
    item = group_items()[index]
    
    details = "\n".join([f"- Location: {loc}" for loc in set(item["locations"])])
    messagebox.showinfo("Item Details", f"Name: {item['name']}\nTotal Quantity: {item['quantity']}\n"
                                        f"Average Expiry Date: {item['avg_expiry']}\nLocations:\n{details}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)
    entry_location.delete(0, tk.END)

# Main Application
root = tk.Tk()
root.title("Grocery List Manager")
root.geometry("600x400")

# Treeview for displaying grouped items
tree = ttk.Treeview(root, columns=("Name", "Quantity", "Avg Expiry Date"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Avg Expiry Date", text="Average Expiry Date")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Button-3>", show_item_details)

# Entry widgets for new items
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(frame)
entry_quantity.grid(row=1, column=1)

tk.Label(frame, text="Expiry Date (YYYY-MM-DD)").grid(row=2, column=0)
entry_expiry = tk.Entry(frame)
entry_expiry.grid(row=2, column=1)

tk.Label(frame, text="Location").grid(row=3, column=0)
entry_location = tk.Entry(frame)
entry_location.grid(row=3, column=1)

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit Item", command=edit_item).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Item", command=delete_item).grid(row=0, column=2, padx=5)

# Populate treeview with grouped data
update_treeview()

root.mainloop()



data_file = 'grocery_data.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {"items": []}

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    expiry_date = entry_expiry.get()
    location = entry_location.get()

    if not name or not quantity or not expiry_date:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Validate the expiry_date format
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Please enter a valid date in the format YYYY-MM-DD.")
        return

    new_item = {
        "name": name,
        "quantity": int(quantity),
        "expiry_date": expiry_date,
        "location": location,
    }
    data["items"].append(new_item)
    save_data()
    update_treeview()
    clear_entries()

def edit_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return
    
    index = int(tree.item(selected_item)["text"])
    data["items"][index] = {
        "name": entry_name.get(),
        "quantity": int(entry_quantity.get()),
        "expiry_date": entry_expiry.get(),
        "location": entry_location.get(),
    }
    save_data()
    update_treeview()
    clear_entries()

def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return
    
    index = int(tree.item(selected_item)["text"])
    del data["items"][index]
    save_data()
    update_treeview()
    clear_entries()

def group_items():
    grouped_data = {}
    for item in data["items"]:
        name = item["name"]
        quantity = item["quantity"]
        expiry_date = datetime.strptime(item["expiry_date"], "%Y-%m-%d")

        if name not in grouped_data:
            grouped_data[name] = {
                "total_quantity": 0,
                "expiry_dates": [],
                "locations": []
            }

        grouped_data[name]["total_quantity"] += quantity
        grouped_data[name]["expiry_dates"].append(expiry_date)
        grouped_data[name]["locations"].append(item["location"])

    grouped_items = []
    for name, details in grouped_data.items():
        # Calculate the average expiry date in timestamps
        avg_timestamp = sum(dt.timestamp() for dt in details["expiry_dates"]) / len(details["expiry_dates"])
        avg_expiry_date = datetime.fromtimestamp(avg_timestamp)
        
        grouped_items.append({
            "name": name,
            "quantity": details["total_quantity"],
            "avg_expiry": avg_expiry_date.strftime("%Y-%m-%d"),
            "locations": details["locations"]
        })
    return grouped_items

def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    for index, item in enumerate(group_items()):
        tree.insert('', 'end', text=index, values=(item["name"], item["quantity"], item["avg_expiry"]))

def show_item_details(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    index = int(tree.item(selected_item)["text"])
    item = group_items()[index]
    
    details = "\n".join([f"- Location: {loc}" for loc in set(item["locations"])])
    messagebox.showinfo("Item Details", f"Name: {item['name']}\nTotal Quantity: {item['quantity']}\n"
                                        f"Average Expiry Date: {item['avg_expiry']}\nLocations:\n{details}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)
    entry_location.delete(0, tk.END)

# Main Application
root = tk.Tk()
root.title("Grocery List Manager")
root.geometry("600x400")

# Treeview for displaying grouped items
tree = ttk.Treeview(root, columns=("Name", "Quantity", "Avg Expiry Date"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Avg Expiry Date", text="Average Expiry Date")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Button-3>", show_item_details)

# Entry widgets for new items
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(frame)
entry_quantity.grid(row=1, column=1)

tk.Label(frame, text="Expiry Date (YYYY-MM-DD)").grid(row=2, column=0)
entry_expiry = tk.Entry(frame)
entry_expiry.grid(row=2, column=1)

tk.Label(frame, text="Location").grid(row=3, column=0)
entry_location = tk.Entry(frame)
entry_location.grid(row=3, column=1)

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit Item", command=edit_item).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Item", command=delete_item).grid(row=0, column=2, padx=5)

# Populate treeview with grouped data
update_treeview()

root.mainloop()



data_file = 'grocery_data.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {"items": []}

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    expiry_date = entry_expiry.get()
    location = entry_location.get()

    if not name or not quantity or not expiry_date:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Validate the expiry_date format
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Please enter a valid date in the format YYYY-MM-DD.")
        return

    new_item = {
        "name": name,
        "quantity": int(quantity),
        "expiry_date": expiry_date,
        "location": location,
    }
    data["items"].append(new_item)
    save_data()
    update_treeview()
    clear_entries()

def edit_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return
    
    index = int(tree.item(selected_item)["text"])
    data["items"][index] = {
        "name": entry_name.get(),
        "quantity": int(entry_quantity.get()),
        "expiry_date": entry_expiry.get(),
        "location": entry_location.get(),
    }
    save_data()
    update_treeview()
    clear_entries()

def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return
    
    index = int(tree.item(selected_item)["text"])
    del data["items"][index]
    save_data()
    update_treeview()
    clear_entries()

def group_items():
    grouped_data = {}
    for item in data["items"]:
        name = item["name"]
        quantity = item["quantity"]
        expiry_date = datetime.strptime(item["expiry_date"], "%Y-%m-%d")

        if name not in grouped_data:
            grouped_data[name] = {
                "total_quantity": 0,
                "expiry_dates": [],
                "locations": []
            }

        grouped_data[name]["total_quantity"] += quantity
        grouped_data[name]["expiry_dates"].append(expiry_date)
        grouped_data[name]["locations"].append(item["location"])

    grouped_items = []
    for name, details in grouped_data.items():
        # Calculate the average expiry date in timestamps
        avg_timestamp = sum(dt.timestamp() for dt in details["expiry_dates"]) / len(details["expiry_dates"])
        avg_expiry_date = datetime.fromtimestamp(avg_timestamp)
        
        grouped_items.append({
            "name": name,
            "quantity": details["total_quantity"],
            "avg_expiry": avg_expiry_date.strftime("%Y-%m-%d"),
            "locations": details["locations"]
        })
    return grouped_items

def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    for index, item in enumerate(group_items()):
        tree.insert('', 'end', text=index, values=(item["name"], item["quantity"], item["avg_expiry"]))

def show_item_details(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    index = int(tree.item(selected_item)["text"])
    item = group_items()[index]
    
    details = "\n".join([f"- Location: {loc}" for loc in set(item["locations"])])
    messagebox.showinfo("Item Details", f"Name: {item['name']}\nTotal Quantity: {item['quantity']}\n"
                                        f"Average Expiry Date: {item['avg_expiry']}\nLocations:\n{details}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)
    entry_location.delete(0, tk.END)

# Main Application
root = tk.Tk()
root.title("Grocery List Manager")
root.geometry("600x400")

# Treeview for displaying grouped items
tree = ttk.Treeview(root, columns=("Name", "Quantity", "Avg Expiry Date"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Avg Expiry Date", text="Average Expiry Date")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Button-3>", show_item_details)

# Entry widgets for new items
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(frame)
entry_quantity.grid(row=1, column=1)

tk.Label(frame, text="Expiry Date (YYYY-MM-DD)").grid(row=2, column=0)
entry_expiry = tk.Entry(frame)
entry_expiry.grid(row=2, column=1)

tk.Label(frame, text="Location").grid(row=3, column=0)
entry_location = tk.Entry(frame)
entry_location.grid(row=3, column=1)

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit Item", command=edit_item).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Item", command=delete_item).grid(row=0, column=2, padx=5)

# Populate treeview with grouped data
update_treeview()

root.mainloop()



data_file = 'grocery_data.json'

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {"items": []}

def save_data():
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

data = load_data()

def add_item():
    name = entry_name.get()
    quantity = entry_quantity.get()
    expiry_date = entry_expiry.get()
    location = entry_location.get()

    if not name or not quantity or not expiry_date:
        messagebox.showwarning("Input Error", "Please fill out all required fields.")
        return

    # Validate the expiry_date format
    try:
        datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Date Format Error", "Please enter a valid date in the format YYYY-MM-DD.")
        return

    new_item = {
        "name": name,
        "quantity": int(quantity),
        "expiry_date": expiry_date,
        "location": location,
    }
    data["items"].append(new_item)
    save_data()
    update_treeview()
    clear_entries()

def edit_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to edit.")
        return
    
    index = int(tree.item(selected_item)["text"])
    data["items"][index] = {
        "name": entry_name.get(),
        "quantity": int(entry_quantity.get()),
        "expiry_date": entry_expiry.get(),
        "location": entry_location.get(),
    }
    save_data()
    update_treeview()
    clear_entries()

def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select an item to delete.")
        return
    
    index = int(tree.item(selected_item)["text"])
    del data["items"][index]
    save_data()
    update_treeview()
    clear_entries()

def group_items():
    grouped_data = {}
    for item in data["items"]:
        name = item["name"]
        quantity = item["quantity"]
        expiry_date = datetime.strptime(item["expiry_date"], "%Y-%m-%d")

        if name not in grouped_data:
            grouped_data[name] = {
                "total_quantity": 0,
                "expiry_dates": [],
                "locations": []
            }

        grouped_data[name]["total_quantity"] += quantity
        grouped_data[name]["expiry_dates"].append(expiry_date)
        grouped_data[name]["locations"].append(item["location"])

    grouped_items = []
    for name, details in grouped_data.items():
        # Calculate the average expiry date in timestamps
        avg_timestamp = sum(dt.timestamp() for dt in details["expiry_dates"]) / len(details["expiry_dates"])
        avg_expiry_date = datetime.fromtimestamp(avg_timestamp)
        
        grouped_items.append({
            "name": name,
            "quantity": details["total_quantity"],
            "avg_expiry": avg_expiry_date.strftime("%Y-%m-%d"),
            "locations": details["locations"]
        })
    return grouped_items

def update_treeview():
    for i in tree.get_children():
        tree.delete(i)
    for index, item in enumerate(group_items()):
        tree.insert('', 'end', text=index, values=(item["name"], item["quantity"], item["avg_expiry"]))

def show_item_details(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    index = int(tree.item(selected_item)["text"])
    item = group_items()[index]
    
    details = "\n".join([f"- Location: {loc}" for loc in set(item["locations"])])
    messagebox.showinfo("Item Details", f"Name: {item['name']}\nTotal Quantity: {item['quantity']}\n"
                                        f"Average Expiry Date: {item['avg_expiry']}\nLocations:\n{details}")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)
    entry_expiry.delete(0, tk.END)
    entry_location.delete(0, tk.END)

# Main Application
root = tk.Tk()
root.title("Grocery List Manager")
root.geometry("600x400")

# Treeview for displaying grouped items
tree = ttk.Treeview(root, columns=("Name", "Quantity", "Avg Expiry Date"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Quantity", text="Quantity")
tree.heading("Avg Expiry Date", text="Average Expiry Date")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Button-3>", show_item_details)

# Entry widgets for new items
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Quantity").grid(row=1, column=0)
entry_quantity = tk.Entry(frame)
entry_quantity.grid(row=1, column=1)

tk.Label(frame, text="Expiry Date (YYYY-MM-DD)").grid(row=2, column=0)
entry_expiry = tk.Entry(frame)
entry_expiry.grid(row=2, column=1)

tk.Label(frame, text="Location").grid(row=3, column=0)
entry_location = tk.Entry(frame)
entry_location.grid(row=3, column=1)

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Item", command=add_item).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Edit Item", command=edit_item).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Item", command=delete_item).grid(row=0, column=2, padx=5)

# Populate treeview with grouped data
update_treeview()

root.mainloop()
