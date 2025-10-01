"""Display pitching stats from CSV file."""
import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.view_utils.scrollable_frame import ScrollableFrame


class PitchStatsApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Pitching Stats")
        self.geometry("1920x1080")

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        self.header_frame = Header(
            self,
            app_name="Pitching Stats",
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(
            self
        )
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        # Main Frame details
        self.stats_frame = DataFrameTableFrame(
            self.main_frame,
        )
        self.stats_frame.grid(row=0, column=0, sticky="nsew")

        self.settings_frame = ScrollableFrame(
            self.main_frame,
        )
        self.settings_frame.grid(row=0, column=1, sticky="nsew")

