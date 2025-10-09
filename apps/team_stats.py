"""App for displaying basic team stats from loaded tournament file."""
import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.view_utils.scrollable_frame import ScrollableFrame

class TeamStatsApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.geometry('1920x1080')
        self.title('Team Stats')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        # Basic page setup
        self.header_frame = Header(
            self,
            app_name='Team Stats',
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.footer_frame = Footer(
            self
        )
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        # Main frame setup
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.stats_frame = DataFrameTableFrame(
            self.main_frame,
        )
        self.stats_frame.grid(row=0, column=0, sticky="nsew")

        self.options_panel = tk.Frame(
            self.main_frame
        )
        self.options_panel.grid(row=0, column=1, sticky="nsew")
        self.options_panel.rowconfigure(0, weight=0)
        self.options_panel.rowconfigure(1, weight=1)
        self.options_panel.columnconfigure(0, weight=1)

        self.button_frame = tk.Frame(
            self.options_panel,
        )
        self.button_frame.grid(row=0, column=0, sticky="nsew")

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=0)
        self.button_frame.columnconfigure(2, weight=1)

        self.load_button = tk.Button(
            self.button_frame,
            text='Reload',
            command=self.reload_data
        )
        self.load_button.grid(row=0, column=1, sticky="nsew")

        self.options_frame = ScrollableFrame(
            self.options_panel,
        )
        self.options_frame.grid(row=1, column=0, sticky="nsew")


    def reload_data(self):
        return