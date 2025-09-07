"""Version 2 of Angered Unicorn's OOTP Tournament Utilities."""
import tkinter as tk
import os
from config_utils.load_save_settings import settings as loaded_settings
from config_utils.load_save_settings import get_setting
from config_utils.select_target_file import select_target_file
from view_utils.header_frame import Header
from view_utils.footer_frame import Footer


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

        # Variables for page
        self.is_card_list_valid = False
        self.target_card_list_var = tk.StringVar(
            value=get_setting('TargetFiles', 'target_card_list')
        )

        # Variables for settings
        self.settings = loaded_settings

        self.card_list_target_path = self.settings['TargetFiles']['target_card_list']
        if not os.path.isfile(self.card_list_target_path):
            self.card_list_target_path = None
            self.is_card_list_valid = False
        elif not self.card_list_target_path.lower().endswith(".csv"):
            self.card_list_target_path = None
            self.is_card_list_valid = False
        else:
            self.is_card_list_valid = True

        # Page rows and columns
        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)

        # Main frames for setting up the page
        row = 0
        self.header_frame = Header(self)
        self.header_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.content_frame = tk.Frame(self, bg='lightgray')
        self.content_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.settings_frame = tk.Label(self, text="Settings", bg='lightgray')
        self.settings_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=row, column=0, sticky="nsew")

        # Content frame configuration
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.columnconfigure(1, weight=1)
        self.content_frame.columnconfigure(2, weight=1)
        self.content_frame.columnconfigure(3, weight=1)

        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.rowconfigure(1, weight=1)
        self.content_frame.rowconfigure(2, weight=0)

        # Settings frame configuration
        self.settings_frame.columnconfigure(0, weight=1)
        self.settings_frame.columnconfigure(1, weight=1)
        self.settings_frame.columnconfigure(2, weight=1)
        self.settings_frame.columnconfigure(3, weight=1)
        self.settings_frame.columnconfigure(4, weight=1)

        # Content frame, buttons for apps and messaging station
        main_row = 0
        main_column = 0

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

        # Settings frame content
        self.select_target_card_list_button = tk.Button(self.settings_frame, text="Select File", command=lambda: select_target_file(self.target_card_list_var))
        self.select_target_card_list_button.grid(row=0, column=0, sticky="w")

        self.card_list_label = tk.Label(self.settings_frame, textvariable=self.target_card_list_var, font=("Arial", 16))
        self.card_list_label.grid(row=0, column=1, sticky="w")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()