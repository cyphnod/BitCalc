import json
import tkinter as tk
from tkinter import messagebox
import csv

HISTORY_FILE = "history.json"

def save_history(data):
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except:
        messagebox.showerror("Error", "Failed to save history.")

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def copy_to_clipboard(text):
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()

def export_csv(data, filename="export.csv"):
    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
        messagebox.showinfo("Export", f"Data exported to {filename}")
    except:
        messagebox.showerror("Error", "Failed to export CSV.")
