import tkinter as tk
from tkinter import ttk

from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.stats_utils.generate_player_stats_for_team_df import generate_player_stats_for_team_df
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame


class TeamCard(tk.Toplevel):
    def __init__(self, selected_team=None):
        super().__init__()

        self.title(f"Team Card for {selected_team}")
        self.geometry("1920x1080")

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        batters, pitchers = generate_player_stats_for_team_df(selected_team)

        self.header_frame = Header(
            self,
            app_name="Team Card for {}".format(selected_team),
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self, background="white")
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        # Frames for stats view
        self.batter_frame = DataFrameTableFrame(self.main_frame, batters)
        self.batter_frame.grid(row=0, column=0, sticky="nsew")

        self.pitcher_frame = DataFrameTableFrame(self.main_frame, pitchers)
        self.pitcher_frame.grid(row=0, column=1, sticky="nsew")