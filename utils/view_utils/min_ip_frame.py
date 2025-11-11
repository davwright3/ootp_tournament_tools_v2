"""Custom frame for setting min innings to display."""
import tkinter as tk


class MinIPFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.min_innings_var = tk.StringVar(value='200')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.min_innings_label = tk.Label(
            self,
            text='Min Innings',
            justify='right'
        )
        self.min_innings_label.grid(row=0, column=0, sticky="e")

        self.min_innings_input = tk.Entry(
            self,
            textvariable=self.min_innings_var,
            justify='left'
        )
        self.min_innings_input.grid(row=0, column=1, sticky="w")

    def get_min_innings(self):
        try:
            selected_min_innings = int(self.min_innings_input.get())
            return selected_min_innings
        except ValueError:
            selected_min_innings = 200
            return selected_min_innings
