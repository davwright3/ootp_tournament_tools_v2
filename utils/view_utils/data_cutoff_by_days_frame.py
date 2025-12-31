import tkinter as tk
from utils.view_utils import program_fonts as fonts


class DataCutoffByDaysFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.days_var = tk.StringVar(value='')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self,
            text="Cutoff Days: ",
        )
        self.label.grid(row=0, column=0, sticky='e')

        self.days_entry = tk.Entry(
            self,
            textvariable=self.days_var,
        )
        self.days_entry.grid(row=0, column=1, sticky='w')

    def get_cutoff_days(self):
        if self.days_var.get() == '':
            return None

        try:
            return int(self.days_entry.get())
        except ValueError:
            return None