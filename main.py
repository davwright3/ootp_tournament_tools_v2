"""Version 2 of Angered Unicorn's OOTP Tournament Utilities."""
import tkinter as tk

class MainApp(tk.Tk):
    """Class for generating the main application."""
    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.title("OOTP Tournament Utils v2")
        self.geometry("640x480")
        self.minsize(400, 300)
        self.configure(bg="lightgray")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()