"""Custom frame for user to select whether they want variants split or not."""
import tkinter as tk


class SplitVariantsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.variant_split_select = tk.BooleanVar(value=False)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self,
            text='Variant Split',
            justify='right'
        )
        self.label.grid(row=0, column=0, sticky='e')

        self.split_select = tk.Checkbutton(
            self,
            variable=self.variant_split_select,
            justify='left'
        )
        self.split_select.grid(row=0, column=1, sticky='w')

    def get_variant_split(self):
        return self.variant_split_select.get()
