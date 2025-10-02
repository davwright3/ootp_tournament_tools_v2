"""Display pitching stats from CSV file."""
import tkinter as tk
from utils.data_utils.data_store import data_store
from utils.stats_utils.generate_basic_pitching_stats_df import generate_basic_pitching_stats
from utils.view_utils import pitcher_type_select_frame
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.view_utils.scrollable_frame import ScrollableFrame
from utils.view_utils.min_max_rating_frame import MinMaxFrame
from utils.view_utils.min_ip_frame import MinIPFrame
from utils.view_utils.pitcher_side_select_frame import PitcherSideSelectFrame
from utils.view_utils.pitcher_type_select_frame import PitcherTypeSelectFrame


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

        self.settings_frame = tk.Frame(
            self.main_frame,
        )
        self.settings_frame.grid(row=0, column=1, sticky="nsew")

        self.settings_frame.columnconfigure(0, weight=1)
        self.settings_frame.rowconfigure(0, weight=0)
        self.settings_frame.rowconfigure(1, weight=1)

        self.reload_button = tk.Button(
            self.settings_frame,
            text="Reload",
            command=self.reload_data
        )
        self.reload_button.grid(row=0, column=0, sticky="nsew")

        self.settings_options_frame = ScrollableFrame(
            self.settings_frame,
        )
        self.settings_options_frame.grid(row=1, column=0, sticky="nsew")

        inner_frame = self.settings_options_frame.inner

        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.rowconfigure(0, weight=0)
        inner_frame.rowconfigure(1, weight=0)
        inner_frame.rowconfigure(2, weight=0)
        inner_frame.rowconfigure(3, weight=0)
        inner_frame.rowconfigure(4, weight=0)
        inner_frame.rowconfigure(5, weight=0)

        row = 0
        self.min_max_ratings_frame = MinMaxFrame(
            inner_frame,
        )
        self.min_max_ratings_frame.grid(row=row, column=0, sticky="ew")
        row += 1

        self.min_innings_frame = MinIPFrame(
            inner_frame
        )
        self.min_innings_frame.grid(row=row, column=0, sticky="ew")
        row += 1

        self.pitcher_side_select_frame = PitcherSideSelectFrame(
            inner_frame,
        )
        self.pitcher_side_select_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.pitcher_type_select_frame = PitcherTypeSelectFrame(
            inner_frame,
        )
        self.pitcher_type_select_frame.grid(row=row, column=0, sticky="nsew")
        row += 1



        stats = generate_basic_pitching_stats()
        self.stats_frame.set_dataframe(stats)

    def reload_data(self):
        stats = generate_basic_pitching_stats()
        self.stats_frame.set_dataframe(stats)
