"""
App for processing multiple csv files into one
via dataframe concatenation.
"""
import tkinter as tk
import logging
import os
from threading import Thread
from utils.config_utils.load_save_settings import settings as loaded_settings
from utils.config_utils.get_resource_path import get_resource_path
from utils.data_utils.create_file_from_template import create_file_from_template
from utils.data_utils.select_return_target_file import select_return_target_file
from utils.data_utils.select_return_data_dir import select_return_data_dir
from utils.dialog_utils.custom_input_dialog import CustomInputDialog
from utils.log_utils.attach import attach_panel
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.message_panel import MessagePanel
from utils.data_utils.process_files import process_files

class FileProcessingApp(tk.Toplevel):
    """File Processing App for csv concatenation via Tkinter GUI."""
    def __init__(self, master=None):
        """Init for the application"""
        super().__init__(master)

        self.geometry("1920x1080")
        self.title("File Processing")

        self.log = logging.getLogger("apps.fileproc")
        self.log.info(f"{self.log} window opened.")

        # Variables for module
        self.starting_ready_folder = (
            loaded_settings['InitialTargetDirs']['starting_target_folder']
        )
        self.starting_data_folder = (
            loaded_settings['InitialTargetDirs']['starting_data_folder']
        )
        self.log.info(f'Ready folder: {self.starting_ready_folder}')
        self.log.info(f'Data folder: {self.starting_data_folder}')

        self.selected_target_file_path_var = tk.StringVar(value='None Selected')
        self.selected_raw_data_path_var = tk.StringVar(value='None Selected')

        # Methods for class
        def _set_process_file_button_state():
            if (self.selected_raw_data_path_var.get() == 'None Selected' or
                    self.selected_target_file_path_var.get() == 'None Selected'):
                self.process_files_button.config(state=tk.DISABLED)
            else:
                self.process_files_button.config(state=tk.NORMAL)

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

        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.rowconfigure(1, weight=0)
        self.main_frame.rowconfigure(2, weight=1)

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
        self.message_panel.grid(row=0, column=1, rowspan=3, sticky="nsew")
        attach_panel(self.message_panel, logger_name="apps.fileproc")

        # Buttons, frames  and info for the file processing frame
        self.new_file_frame = tk.Frame(self.main_frame, bg='lightgray', relief='ridge', bd=3)
        self.new_file_frame.grid(row=0, column=0, sticky="nsew", pady=(2, 10))

        self.process_files_frame = tk.Frame(self.main_frame, bg='lightgray', relief='ridge', bd=3)
        self.process_files_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 3))

        self.process_files_frame.columnconfigure(0, weight=0)
        self.process_files_frame.columnconfigure(1, weight=0)
        self.process_files_frame.columnconfigure(2, weight=1)

        self.new_file_button = tk.Button(
            self.new_file_frame,
            text="New File",
            command=lambda: create_file_from_template(self)
        )
        self.new_file_button.grid(row=0, column=0, sticky="nsew", pady=3)

        self.new_file_label = tk.Label(
            self.new_file_frame,
            text = f'Create a new file from template.  FIle will be copied to {self.starting_ready_folder}',
            font = ('Arial', 12),
            bg='lightgray'
        )
        self.new_file_label.grid(row=0, column=1, sticky="nsew")

        self.select_target_file_button = tk.Button(
            self.process_files_frame,
            text="Select Target File",
            command=lambda: (select_return_target_file(self, self.selected_target_file_path_var),
                             _set_process_file_button_state())
        )
        self.select_target_file_button.grid(row=0, column=0, sticky="e", pady=3, padx=(2, 5))

        self.select_target_file_info_label = tk.Label(
            self.process_files_frame,
            text= 'Select target file.  This will be the file that the data gets processed into.',
            font = ('Arial', 12),
            bg='lightgray'
        )
        self.select_target_file_info_label.grid(row=0, column=1, sticky="w")

        self.selected_target_file_label = tk.Label(
            self.process_files_frame,
            textvariable=self.selected_target_file_path_var,
            font = ('Arial', 8),
            bg='lightgray'
        )
        self.selected_target_file_label.grid(row=0, column=2, sticky="e")

        self.select_data_folder_button = tk.Button(
            self.process_files_frame,
            text="Select Data Folder",
            command=lambda: (select_return_data_dir(self, self.selected_raw_data_path_var),
                             _set_process_file_button_state())
        )
        self.select_data_folder_button.grid(row=1, column=0, sticky="e", pady=3, padx=(2, 5))

        self.select_data_folder_info_label = tk.Label(
            self.process_files_frame,
            text='Select folder where data will be copied from.',
            font = ('Arial', 12),
            bg='lightgray'
        )
        self.select_data_folder_info_label.grid(row=1, column=1, sticky="w")

        self.selected_data_folder_path_label = tk.Label(
            self.process_files_frame,
            textvariable=self.selected_raw_data_path_var,
            font = ('Arial', 8),
            bg='lightgray'
        )
        self.selected_data_folder_path_label.grid(row=1, column=2, sticky="e")

        self.process_files_button = tk.Button(
            self.process_files_frame,
            text="Process Files",
            command=self.start_processing
        )
        self.process_files_button.grid(row=2, column=0, sticky="e", pady=3, padx=(2, 5))

        self.process_files_label = tk.Label(
            self.process_files_frame,
            text='Process files from data folder into target file.',
            font = ('Arial', 12),
            bg='lightgray'
        )
        self.process_files_label.grid(row=2, column=1, sticky="w")

        _set_process_file_button_state()

    def start_processing(self):
        logger = logging.getLogger("apps.fileproc")
        target_path = self.selected_target_file_path_var.get()
        raw_data_path = self.selected_raw_data_path_var.get()

        Thread(target=process_files, args=(target_path, raw_data_path), daemon=True).start()
        logger.info("Start background processing.")




