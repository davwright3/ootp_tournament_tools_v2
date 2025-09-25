"""Custom frame for selecting and returning min and max ratings."""
import tkinter as tk


class MinMaxFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.label = tk.Label(self, text="Min and Max Ratings")
        self.label.grid(column=0, row=0, sticky='nsew')