import tkinter as tk
from utils.view_utils import program_fonts as fonts


class StatLabel(tk.Frame):
    def __init__(self, parent, label_name, stat):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.label = tk.Label(
            self,
            text=label_name,
            font=fonts.basic_font
        )
        self.label.grid(row=0, column=0, sticky='e')

        self.stat_label = tk.Label(
            self,
            text=stat,
            font=fonts.basic_font
        )
        self.stat_label.grid(row=0, column=1, sticky='w')
