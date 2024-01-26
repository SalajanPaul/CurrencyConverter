from currency_converter import CurrencyConverter
from datetime import date
import tkinter as tk
c = CurrencyConverter()

class Converter:
    def __init__(self):
        self.money = None
        self.root = tk.Tk()

        self.convert_button = tk.Button(self.root, text="Convert", font=("Arial", 16),command=self.exchange)
        self.convert_button.pack(padx=10, pady=10)

        self.root.mainloop()

    def exchange(self):
        print(c.convert(100, "RON", "EUR"))

Converter()

