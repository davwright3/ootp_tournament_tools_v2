"""Custom frame for player or team search functionality."""
import tkinter as tk


class SearchFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.search_term = tk.StringVar(value='')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self,
            text="Search",
            justify='right'
        )
        self.label.grid(row=0, column=0, sticky='e')

        self.search_entry = tk.Entry(
            self,
            textvariable=self.search_term,
            justify='left'
        )
        self.search_entry.grid(row=0, column=1, sticky='w')

    def get_search_term(self):
        if self.search_term.get() == '':
            return None
        else:
            return self.search_term.get()
