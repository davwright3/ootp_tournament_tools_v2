"""App for comparing ratings of selected players."""
import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer


class RatingsComparisonApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Ratings Comparison")
        self.geometry("1920x1080")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.header_frame = Header(self)
        self.header_frame.grid(column=0, row=0, sticky='nsew')

        self.footer_frame = Footer(self)
        self.footer_frame.grid(column=0, row=2, sticky='nsew')

