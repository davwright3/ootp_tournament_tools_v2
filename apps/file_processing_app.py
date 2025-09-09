"""
App for processing multiple csv files into one
via dataframe concatenation.
"""
import tkinter as tk
import logging
from config_utils.load_save_settings import settings as loaded_settings
from log_utils.attach import attach_panel
from view_utils.header_frame import Header
from view_utils.footer_frame import Footer
from view_utils.message_panel import MessagePanel
from data_utils.process_fiies import process_files


class FileProcessingApp(tk.Toplevel):
    """File Processing App for csv concatenation via Tkinter GUI."""
    def __init__(self, master=None):
        """Init for the application"""
        super().__init__(master)

        self.geometry("1920x1080")
        self.title("File Processing")

        # Variables for module
        self.starting_ready_folder = (
            loaded_settings['InitialTargetDirs']['starting_target_folder']
        )
        self.starting_data_folder = (
            loaded_settings['InitialTargetDirs']['starting_data_folder']
        )

        # Set up the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        # Set up the frames
        self.header_frame = Header(
            self,
            app_name="File Processing"
        )
        self.header_frame.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="nsew"
        )

        self.main_frame = tk.Frame(self, bg='lightgray')
        self.main_frame.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="nsew"
        )

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)

        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(
            row=2,
            column=0,
            columnspan=3,
            sticky="nsew"
        )

        # Panels for main frame (select file and buttons panel, and messaging panel)
        self.file_processing_panel = tk.Frame(
            self.main_frame,
        )
        self.file_processing_panel.grid(row=0, column=0, sticky="nsew")

        self.message_panel = MessagePanel(
            self.main_frame,
        )
        self.message_panel.grid(row=0, column=1, sticky="nsew")
        attach_panel(self.message_panel, logger_name="apps.fileproc")

        self.log = logging.getLogger("apps.fileproc")
        self.log.info(f"{self.log} window opened.")
        self.log.info(f'Current ready data folder: {self.starting_ready_folder}')
        self.log.info(f'Current data folder: {self.starting_data_folder}')

        # Buttons and info for the file processing frame
        self.process_files_button = tk.Button(
            self.file_processing_panel,
            text="Process Files",
            command=process_files
        )
        self.process_files_button.grid(row=0, column=0, sticky="nsew")
