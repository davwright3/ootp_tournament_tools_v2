import tkinter as tk
from tkinter import ttk


class MessagePanel(ttk.Frame):
    def __init__(self, parent, *, height=10, wrap="word"):
        super().__init__(parent)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.text = tk.Text(
            self, height=height, wrap=wrap, state='disabled')
        self.text.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(
            self, orient='vertical', command=self.text.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.text.configure(yscrollcommand=self.scrollbar.set)

        # Tags
        self.text.tag_config('INFO', foreground='royal blue')
        self.text.tag_config('ERROR', foreground='firebrick')
        self.text.tag_config('WARNING', foreground='orange')

    def append(self, msg, tag=None):
        self.text.configure(state='normal')
        if tag:
            self.text.insert('end', msg + "\n", (tag,))
        else:
            self.text.insert('end', msg + "\n")
        self.text.see('end')
        self.text.configure(state='disabled')
