"""Version 2 of Angered Unicorn's OOTP Tournament Utilities."""
import tkinter as tk
from config_utils.load_settings import settings as loaded_settings
from view_utils.header_view import Header

class MainApp(tk.Tk):
    """Class for generating the main application."""
    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.title("OOTP Tournament Utils v2")
        self.geometry("1920x1080")
        self.minsize(400, 300)
        self.configure(bg="lightgray")

        settings = loaded_settings

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        row = 0
        self.header_frame = Header(self)
        self.header_frame.grid(row=row, column=0, sticky="nsew")
        row += 1







if __name__ == "__main__":
    app = MainApp()
    app.mainloop()