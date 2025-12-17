import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.data_utils.data_store import data_store


class BatterSlideshowApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Batting Leaders')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        self.header_frame = Header(
            self,
            app_name="Batting Leaders"
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        # Get the starting dataframe

