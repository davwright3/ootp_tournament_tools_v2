"""Version 2 of Angered Unicorn's OOTP Tournament Utilities."""
import tkinter as tk
import os
import logging
import sys
from logging.handlers import MemoryHandler
from utils.config_utils.load_save_settings import (
    settings as loaded_settings
)
from utils.config_utils.load_save_settings import get_setting
from utils.config_utils.select_starting_folder_dirs import (
    select_initial_target_folder, select_initial_raw_data_folder
)
from utils.log_utils.readme_messaging import log_readme_section
from utils.config_utils.get_base_resource_path import (
    get_base_resource_path
)
from utils.config_utils.select_target_card_list_file import select_target_file
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.message_panel import MessagePanel
from utils.log_utils.tk_handler import TkTextHandler
from apps.file_processing_app import FileProcessingApp
from apps.basic_stats_app import BasicStatsApp

root = logging.getLogger()
root.setLevel(logging.INFO)
BOOTSTRAP_MEM = MemoryHandler(
    capacity=10000,
    flushLevel=logging.CRITICAL
)
root.addHandler(BOOTSTRAP_MEM)


class ExcludeNamespaces(logging.Filter):
    def __init__(self, *prefixes: str):
        super().__init__()
        self.prefixes = prefixes

    def filter(self, record: logging.LogRecord) -> bool:
        return not any(record.name.startswith(p) for p in self.prefixes)


class MainApp(tk.Tk):
    """Class for generating the main application."""
    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.title("OOTP Tournament Utils v2")
        self.geometry("1920x1080")
        self.minsize(400, 300)
        self.configure(bg="lightgray")

        # Variables for page
        self.target_card_list_var = tk.StringVar(
            value=get_setting('TargetFiles', 'target_card_list')
        )
        self.initial_target_folder_var = tk.StringVar(
            value=get_setting(
                'InitialTargetDirs',
                'starting_target_folder'
            )
        )
        self.initial_raw_data_folder_var = tk.StringVar(
            value=get_setting(
                'InitialTargetDirs',
                'starting_data_folder'
            )
        )

        self.is_card_list_valid = tk.BooleanVar(value=False)
        self.card_list_valid_display = tk.StringVar()

        # Variables for settings
        self.settings = loaded_settings

        self.card_list_target_path = (
            self.settings['TargetFiles']['target_card_list']
        )

        # Page rows and columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)

        # Main frames for setting up the page
        row = 0
        self.header_frame = Header(self)
        self.header_frame.grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="nsew"
        )
        row += 1

        self.content_frame = tk.Frame(self, bg='red')
        self.content_frame.grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="nsew"
        )
        row += 1

        self.settings_frame = tk.Frame(
            self,
            bg='lightgray',
            relief='groove',
            bd=3
        )
        self.settings_frame.grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="nsew"
        )
        row += 1

        self.footer_frame = Footer(self)
        self.footer_frame.grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        # Content frame configuration
        self.content_frame.columnconfigure(0, weight=1)
        self.content_frame.columnconfigure(1, weight=1)

        self.content_frame.rowconfigure(0, weight=1)

        # Settings frame configuration
        self.settings_frame.grid_columnconfigure(0, weight=0)
        self.settings_frame.grid_columnconfigure(1, weight=0)
        self.settings_frame.grid_columnconfigure(2, weight=0)
        self.settings_frame.grid_columnconfigure(3, weight=0)
        self.settings_frame.grid_columnconfigure(4, weight=1)

        self.settings_frame.grid_rowconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(1, weight=1)
        self.settings_frame.grid_rowconfigure(2, weight=1)

        # Frames inside of content frame
        self.buttons_frame = tk.Frame(self.content_frame, bg='red')
        self.buttons_frame.grid(row=0, column=0, sticky="nsew")

        def check_card_list_valid():
            if not os.path.isfile(str(self.card_list_target_path)):
                self.card_list_target_path = None
                self.card_list_valid_display.set("Invalid \u274c")
                for widget in self.buttons_frame.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.configure(state=tk.DISABLED)
            elif not self.card_list_target_path.lower().endswith(".csv"):
                self.card_list_target_path = None
                self.card_list_valid_display.set("Invalid \u274c")
                for widget in self.buttons_frame.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.configure(state=tk.DISABLED)
            else:
                self.card_list_valid_display.set("Valid \u2713")
                for widget in self.buttons_frame.winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.configure(state=tk.NORMAL)

        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)
        self.buttons_frame.columnconfigure(2, weight=1)

        self.buttons_frame.rowconfigure(0, weight=1)
        self.buttons_frame.rowconfigure(1, weight=1)
        self.buttons_frame.rowconfigure(2, weight=1)

        self.message_frame = tk.Frame(self.content_frame, bg='blue')
        self.message_frame.grid(row=0, column=1, sticky="nsew")

        self.message_frame.grid_columnconfigure(0, weight=1)
        self.message_frame.grid_rowconfigure(0, weight=1)

        # Content frame, buttons for apps and messaging station
        main_row = 0
        main_column = 0

        self.file_processing_button = tk.Button(
            self.buttons_frame,
            text="File Processing",
            command=open_file_processing_app,
            padx=5,
            pady=5,
        )
        self.file_processing_button.grid(
            row=int(main_row / 3),
            column=main_column % 3,
            sticky="nsew"
        )
        main_row += 1
        main_column += 1

        self.basic_stats_app_button = tk.Button(
            self.buttons_frame,
            text="Basic Stats App",
            command=open_basic_stats_app,
            padx=5,
            pady=5,
        )
        self.basic_stats_app_button.grid(
            row=int(main_row / 3),
            column=main_column % 3,
            sticky="nsew"
        )
        main_row += 1
        main_column += 1

        self.message_panel = MessagePanel(self.message_frame, height=12)
        self.message_panel.grid(row=0, column=0, sticky="nsew")

        def on_select_card_file():
            select_target_file()
            self.card_list_target_path = (
                self.settings.get(
                    'TargetFiles',
                    'target_card_list',
                    fallback='')
            )
            self.target_card_list_var.set(self.card_list_target_path)
            check_card_list_valid()

        # Settings frame content
        self.select_target_card_list_button = tk.Button(
            self.settings_frame,
            text="Select File",
            command=on_select_card_file,
        )
        self.select_target_card_list_button.grid(
            row=0, column=0, sticky="w", padx=3, pady=3)

        self.card_list_label = tk.Label(
            self.settings_frame,
            text="Card List:",
            font=('Arial', 10, 'bold'),
            bg='lightgray'
        )
        self.card_list_label.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=3,
            pady=3
        )

        self.card_list_target_location_label = tk.Label(
            self.settings_frame,
            textvariable=self.target_card_list_var,
            font=("Arial", 10),
            bg='lightgray'
        )
        self.card_list_target_location_label.grid(
            row=0,
            column=2,
            sticky="w",
            padx=3,
            pady=3
        )

        self.select_initial_target_file_dir_button = tk.Button(
            self.settings_frame,
            text="Select File",
            command=lambda: (
                select_initial_target_folder(
                    self,
                    self.initial_target_folder_var)
            )
        )
        self.select_initial_target_file_dir_button.grid(
            row=1,
            column=0,
            sticky="w",
            padx=3,
            pady=3
        )

        self.initial_target_data_label = tk.Label(
            self.settings_frame,
            text="Tgt Data:",
            font=("Arial", 10, 'bold'),
            bg='lightgray'
        )
        self.initial_target_data_label.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=3,
            pady=3
        )

        self.select_initial_target_folder_location_label = tk.Label(
            self.settings_frame,
            textvariable=self.initial_target_folder_var,
            font=("Arial", 10),
            bg='lightgray'
        )
        self.select_initial_target_folder_location_label.grid(
            row=1,
            column=2,
            sticky="w",
            padx=3,
            pady=3
        )

        self.select_initial_raw_data_folder_button = tk.Button(
            self.settings_frame,
            text="Select File",
            command=lambda: (
                select_initial_raw_data_folder(
                    self,
                    self.initial_raw_data_folder_var)
            )
        )
        self.select_initial_raw_data_folder_button.grid(
            row=2,
            column=0,
            sticky="w",
            padx=3,
            pady=3
        )

        self.initial_raw_data_folder_label = tk.Label(
            self.settings_frame,
            text="Raw Data:",
            font=("Arial", 10, 'bold'),
            bg='lightgray'
        )
        self.initial_raw_data_folder_label.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=3,
            pady=3
        )

        self.select_initial_raw_data_folder_location_label = tk.Label(
            self.settings_frame,
            textvariable=self.initial_raw_data_folder_var,
            font=("Arial", 10),
            bg='lightgray'
        )
        self.select_initial_raw_data_folder_location_label.grid(
            row=2,
            column=2,
            sticky="w",
            padx=3,
            pady=3
        )

        self.card_list_valid_label = tk.Label(
            self.settings_frame,
            textvariable=self.card_list_valid_display,
            font=("Arial", 10, 'bold')
        )
        self.card_list_valid_label.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=3,
            pady=3
        )

        check_card_list_valid()

        # Logging info
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)

        ui_handler = TkTextHandler(self.message_panel)
        ui_handler.setFormatter(logging.Formatter(fmt='%(message)s'))

        ui_handler.addFilter(ExcludeNamespaces(
            "apps.fileproc",
            'apps.basic_stats_app'
            )
        )
        root_logger.addHandler(ui_handler)

        BOOTSTRAP_MEM.setTarget(ui_handler)
        BOOTSTRAP_MEM.flush()
        root.removeHandler(BOOTSTRAP_MEM)

        logging.info("Thank you for using my OOTP "
                     "Tournament Statistics Utility Tool")

        readme_file = get_base_resource_path("README.md")
        log_readme_section(readme_file, 'Updated:')

        try:
            import utils.data_utils.mlb_season_stats_store as mlb_mod
            logging.info("Loaded MLB historical data as season stats.")
        except:
            logging.info("Failed to import mlb_season_stats_store")


def open_file_processing_app():
    logging.info("Opening file processing app..")
    FileProcessingApp()


def open_basic_stats_app():
    logging.info("Opening basic stats app..")
    BasicStatsApp()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
