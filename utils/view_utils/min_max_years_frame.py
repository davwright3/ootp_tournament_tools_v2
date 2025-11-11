"""Modular frame for selecting min and max years of cards to view."""
import tkinter as tk
from tkinter import ttk


class MinMaxYearsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.min_year = tk.StringVar(value='1871')
        self.max_year = tk.StringVar(value='2025')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        row = 0
        self.label = tk.Label(self, text='Min and Max Years')
        self.label.grid(column=0, row=row, sticky='nsew', columnspan=2)
        row += 1

        self.min_year_label = ttk.Label(self, text='Min Year')
        self.min_year_label.grid(column=0, row=row, sticky='e')

        self.min_year_entry = ttk.Entry(
            self,
            textvariable=self.min_year,
            width=10
        )
        self.min_year_entry.grid(column=1, row=row, sticky='w')
        row += 1

        self.max_year_label = ttk.Label(self, text='Max Year')
        self.max_year_label.grid(column=0, row=row, sticky='e')

        self.max_year_entry = ttk.Entry(
            self,
            textvariable=self.max_year,
            width=10,
        )
        self.max_year_entry.grid(column=1, row=row, sticky='w')
        row += 1

    def get_min_max_years(self):
        try:
            min_year_num = int(self.min_year.get())
        except ValueError:
            min_year_num = 1871

        try:
            max_year_num = int(self.max_year.get())
        except ValueError:
            max_year_num = 2025

        return min_year_num, max_year_num
