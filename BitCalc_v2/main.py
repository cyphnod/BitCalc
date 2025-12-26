import tkinter as tk
from tkinter import ttk, messagebox

# ---- Calculator functions ----


def position_size(balance, risk_percent, stop_loss):
    try:
        balance = float(balance)
        risk_percent = float(risk_percent)
        stop_loss = float(stop_loss)
        size = (balance * (risk_percent / 100)) / stop_loss
        return round(size, 2)
    except:
        return "Invalid Input"

# Main GUI


class TradingCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trading Calculator V2 / BitCalc")
        self.geometry("400x300")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand = 1, fill="both")
