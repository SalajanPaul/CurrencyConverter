from tkinter import messagebox
from currency_converter import CurrencyConverter
from datetime import date
import tkinter as tk
c = CurrencyConverter()

class Converter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Exchange")

        options_list1 = ["RON", "EUR", "RUB", "USD"]
        options_list2 = ["1", "2", "3", "4"]

        value_inside = tk.StringVar(self.root)
        value_inside.set("Select an Option")

        question_meniu1 = tk.OptionMenu(self.root, value_inside, *options_list1)
        question_meniu1.pack()

        question_meniu2 = tk.OptionMenu(self.root, value_inside, *options_list2)
        question_meniu2.pack()

        self.convert_button = tk.Button(self.root, text="Convert", font=("Arial", 16), command=self.exchange)
        self.convert_button.pack(padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.result_label.pack(pady=50, padx=150)

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

        self.root.mainloop()

    def exchange(self):
        result = c.convert(100, "RON", "EUR", date=date(2024, 1, 2))
        result_round = round(result)
        self.result_label.config(text=f"{result_round}")

    def close_app(self):
        if messagebox.askyesno(title="Quit", message="Do you really want to quit?"):
            self.root.destroy()




Converter()

