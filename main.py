from currency_converter import CurrencyConverter
from datetime import date
import tkinter as tk
c = CurrencyConverter()

class Converter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Exchange")

        self.convert_button = tk.Button(self.root, text="Convert", font=("Arial", 16), command=self.exchange)
        self.convert_button.pack(padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.result_label.pack(pady=50, padx=150)

        self.root.mainloop()

    def exchange(self):
        result = c.convert(100, "RON", "EUR", date=date(2024, 1, 2))
        result_round = round(result)
        self.result_label.config(text=f"{result_round}")


Converter()

