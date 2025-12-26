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

        # position size tab

        self.tab_position = ttk.Frame(self.tabs)
        self.tabs.add(self.tab_position, text="Position Size")

        self.create_position_tab()

    def create_position_tab(self):
        tk.Label(self.tab_position, text="Account Balance:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.tab_position, text="Risk %:").grid(row=1, column=0, padx=10, padxy=10)
        tk.Label(self.tab_position, text="Stop Loss:").grid(row=2, column=0, padx=10, pady=10)

        self.balance_entry = tk.Entry(self.tab_position)
        self.risk_entry = tk.Entry(self.tab_position)
        self.stop_entry = tk.Entry(self.tab_position)

        self.balance_entry.grid(row=0, column=1)
        self.risk_entry.grid(row=1, column=1)
        self.stop_entry.grid(row=2, column=1)

        tk.Button(self.tab_position, text="Calculate", command=self.calculate_position).grid(row=3, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(self.tab_position, text="Position size: ")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_position(self):
        balance = self.balance_entry.get()
        risk = self.risky_entry.get()
        stop = self.stop_entry.get()
        result = position_size(balance, risk, stop)
        self.result_label.config(text=f"Position Size: {result}")

if __name__ == "__main__":
    app = TradingCalculator()
    app.mainloop()
