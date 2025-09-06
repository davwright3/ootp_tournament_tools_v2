"""Version 2 of Angered Unicorn's OOTP Tournament Utilities."""
import tkinter as tk
from config_utils.load_settings import settings as loaded_settings
from view_utils.header_view import Header
from view_utils.footer_view import Footer

class MainApp(tk.Tk):
    """Class for generating the main application."""
    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.title("OOTP Tournament Utils v2")
        self.geometry("1920x1080")
        self.minsize(400, 300)
        self.configure(bg="lightgray")

        def open_file_processing_app():
            print("Opening file processing app..")

        settings = loaded_settings

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        # Main frames for setting up the page
        row = 0
        self.header_frame = Header(self)
        self.header_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.content_frame = tk.Frame(self, bg='lightgray')
        self.content_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=row, column=0, sticky="nsew")

        # Buttons for apps

        main_row = 0
        main_column = 0

        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.columnconfigure(1, weight=1)
        self.content_frame.columnconfigure(2, weight=1)
        self.content_frame.columnconfigure(3, weight=1)

        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.rowconfigure(1, weight=1)
        self.content_frame.rowconfigure(2, weight=1)

        self.file_processing_button = tk.Button(
            self.content_frame,
            text="File Processing",
            command=open_file_processing_app,
            padx=5,
            pady=5,
        )
        self.file_processing_button.grid(row=int(main_row / 4), column=main_column % 4, sticky="nsew")
        main_row += 1
        main_column += 1



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()