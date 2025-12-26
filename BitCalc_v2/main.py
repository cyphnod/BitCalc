import tkinter as tk
from tkinter import ttk, messagebox
from calculators import position_size, profit_loss, leverage_position
from utils import save_history, load_history, copy_to_clipboard, export_csv

history = load_history()

class TradingCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Trading Calculator v2")
        self.geometry("500x400")

        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=1, fill="both")

        # --- Tabs ---
        self.tab_position = ttk.Frame(self.tabs)
        self.tab_profit = ttk.Frame(self.tabs)
        self.tab_leverage = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_position, text="Position Size")
        self.tabs.add(self.tab_profit, text="Profit/Loss")
        self.tabs.add(self.tab_leverage, text="Leverage")

        # Create each tab UI
        self.create_position_tab()
        self.create_profit_tab()
        self.create_leverage_tab()

    # --- Position Size Tab ---
    def create_position_tab(self):
        tk.Label(self.tab_position, text="Balance:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.tab_position, text="Risk %:").grid(row=1, column=0)
        tk.Label(self.tab_position, text="Stop Loss:").grid(row=2, column=0)

        self.balance_entry = tk.Entry(self.tab_position)
        self.risk_entry = tk.Entry(self.tab_position)
        self.stop_entry = tk.Entry(self.tab_position)

        self.balance_entry.grid(row=0, column=1)
        self.risk_entry.grid(row=1, column=1)
        self.stop_entry.grid(row=2, column=1)

        tk.Button(self.tab_position, text="Calculate", command=self.calc_position).grid(row=3, column=0, columnspan=2, pady=10)
        self.pos_result = tk.Label(self.tab_position, text="Position Size: ")
        self.pos_result.grid(row=4, column=0, columnspan=2)

        tk.Button(self.tab_position, text="Copy Result", command=lambda: copy_to_clipboard(self.pos_result.cget("text"))).grid(row=5, column=0, columnspan=2)
    
    def calc_position(self):
        b = self.balance_entry.get()
        r = self.risk_entry.get()
        s = self.stop_entry.get()
        result = position_size(b, r, s)
        if result is None:
            self.pos_result.config(text="Invalid input")
        else:
            self.pos_result.config(text=f"Position Size: {result}")
            history.append({"type":"position_size", "balance":b,"risk":r,"stop_loss":s,"result":result})
            save_history(history)

    # --- Profit/Loss Tab ---
    def create_profit_tab(self):
        tk.Label(self.tab_profit, text="Entry Price:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.tab_profit, text="Exit Price:").grid(row=1, column=0)
        tk.Label(self.tab_profit, text="Position Size:").grid(row=2, column=0)

        self.entry_entry = tk.Entry(self.tab_profit)
        self.exit_entry = tk.Entry(self.tab_profit)
        self.size_entry = tk.Entry(self.tab_profit)

        self.entry_entry.grid(row=0, column=1)
        self.exit_entry.grid(row=1, column=1)
        self.size_entry.grid(row=2, column=1)

        tk.Button(self.tab_profit, text="Calculate P/L", command=self.calc_profit).grid(row=3, column=0, columnspan=2, pady=10)
        self.pl_result = tk.Label(self.tab_profit, text="Profit/Loss: ")
        self.pl_result.grid(row=4, column=0, columnspan=2)

        tk.Button(self.tab_profit, text="Copy Result", command=lambda: copy_to_clipboard(self.pl_result.cget("text"))).grid(row=5, column=0, columnspan=2)

    def calc_profit(self):
        e = self.entry_entry.get()
        x = self.exit_entry.get()
        s = self.size_entry.get()
        result = profit_loss(e, x, s)
        if result is None:
            self.pl_result.config(text="Invalid input")
        else:
            self.pl_result.config(text=f"Profit/Loss: {result}")
            history.append({"type":"profit_loss", "entry":e,"exit":x,"size":s,"result":result})
            save_history(history)

    # --- Leverage Tab ---
    def create_leverage_tab(self):
        tk.Label(self.tab_leverage, text="Balance:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.tab_leverage, text="Leverage:").grid(row=1, column=0)
        tk.Label(self.tab_leverage, text="Risk %:").grid(row=2, column=0)
        tk.Label(self.tab_leverage, text="Stop Loss:").grid(row=3, column=0)

        self.l_balance = tk.Entry(self.tab_leverage)
        self.l_leverage = tk.Entry(self.tab_leverage)
        self.l_risk = tk.Entry(self.tab_leverage)
        self.l_stop = tk.Entry(self.tab_leverage)

        self.l_balance.grid(row=0, column=1)
        self.l_leverage.grid(row=1, column=1)
        self.l_risk.grid(row=2, column=1)
        self.l_stop.grid(row=3, column=1)

        tk.Button(self.tab_leverage, text="Calculate", command=self.calc_leverage).grid(row=4, column=0, columnspan=2, pady=10)
        self.l_result = tk.Label(self.tab_leverage, text="Position Size (Leverage): ")
        self.l_result.grid(row=5, column=0, columnspan=2)

        tk.Button(self.tab_leverage, text="Copy Result", command=lambda: copy_to_clipboard(self.l_result.cget("text"))).grid(row=6, column=0, columnspan=2)

    def calc_leverage(self):
        b = self.l_balance.get()
        l = self.l_leverage.get()
        r = self.l_risk.get()
        s = self.l_stop.get()
        result = leverage_position(b, l, r, s)
        if result is None:
            self.l_result.config(text="Invalid input")
        else:
            self.l_result.config(text=f"Position Size (Leverage): {result}")
            history.append({"type":"leverage","balance":b,"leverage":l,"risk":r,"stop_loss":s,"result":result})
            save_history(history)

if __name__ == "__main__":
    app = TradingCalculator()
    app.mainloop()
