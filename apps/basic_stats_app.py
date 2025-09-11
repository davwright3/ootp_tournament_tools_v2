"""
App for viewing basic hitting, pitching and team stats.
Loads a dataframe singleton for opening apps for specific categories.
"""
import tkinter as tk
import logging
import os
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.data_utils.select_return_stats_data_file import select_return_stats_data_file
from utils.view_utils.message_panel import MessagePanel
from utils.log_utils.attach import attach_panel



class BasicStatsApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Basic Stats Views")
        self.geometry("1920x1080")

        # Variables for page
        self.data_file_select_var = tk.StringVar(value=None)
        self.dataframe_loaded_var = tk.StringVar(value="No file selected.")
        self.is_dataframe_loaded = False

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        self.columnconfigure(0, weight=1)

        # Main frames for page (header, footer, data file selection, app select)
        self.header_frame = Header(self)
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.select_data_file_frame = tk.Frame(
            self,
            bg='lightgray',
            relief='ridge',
            bd=3
        )
        self.select_data_file_frame.grid(row=1, column=0, sticky="nsew")

        self.select_data_file_frame.columnconfigure(0, weight=0)
        self.select_data_file_frame.columnconfigure(1, weight=1)
        self.select_data_file_frame.columnconfigure(2, weight=1)
        self.select_data_file_frame.columnconfigure(3, weight=1)

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=2, column=0, sticky="nsew")

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=3, column=0, sticky="nsew")

        # Data for file selection frame
        self.data_file_select_button = tk.Button(
            self.select_data_file_frame,
            text="File Select",
            command=lambda: select_return_stats_data_file(self)
        )
        self.data_file_select_button.grid(row=0, column=0, sticky="e")

        self.data_file_select_info_label = tk.Label(
            self.select_data_file_frame,
            text="Select data file to load.  File must be CSV, and will be set as a DataFrame singleton.",
            font=("Arial", 12),
            bg="lightgray",
        )
        self.data_file_select_info_label.grid(row=0, column=1, sticky="w")

        self.valid_file_label = tk.Label(
            self.select_data_file_frame,
            textvariable=self.dataframe_loaded_var,
            font=("Arial", 12),
            bg="lightgray",
        )
        self.valid_file_label.grid(row=0, column=3, sticky="e")

        # Data for main frame
        self.message_panel = MessagePanel(self.main_frame, height=12)
        self.message_panel.grid(row=0, column=1, sticky="nsew")
        attach_panel(self.message_panel, 'apps.basic_stats_app')
        self.log = logging.getLogger("apps.basic_stats_app")
        self.log.info("Initializing Basic Stats App")

