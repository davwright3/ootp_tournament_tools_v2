"""Custom frame for selecting and returning min and max ratings."""
import tkinter as tk


class MinMaxFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.min_rating = tk.StringVar(value='40')
        self.max_rating = tk.StringVar(value='105')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)

        self.label = tk.Label(
            self, text="Min and Max Ratings", justify='center')
        self.label.grid(column=1, row=0, columnspan=2, sticky='nsew')

        self.min_label = tk.Label(self, text="Min")
        self.min_label.grid(column=1, row=1, sticky='nsew')

        self.min_rating = tk.Entry(
            self, textvariable=self.min_rating, width=10)
        self.min_rating.grid(column=1, row=2, sticky='nsew')

        self.max_label = tk.Label(self, text="Max")
        self.max_label.grid(column=2, row=1, sticky='nsew')

        self.max_rating = tk.Entry(
            self, textvariable=self.max_rating, width=10)
        self.max_rating.grid(column=2, row=2, sticky='nsew')

    def get_min_max_rating(self):
        try:
            min_rating = int(self.min_rating.get())
        except ValueError:
            min_rating = 40
        try:
            max_rating = int(self.max_rating.get())
        except ValueError:
            max_rating = 105
        return min_rating, max_rating
