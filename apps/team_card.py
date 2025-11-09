import tkinter as tk
from tkinter import ttk
import pandas as pd

from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.stats_utils.generate_player_stats_for_team_df import generate_player_stats_for_team_df
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from apps.batter_card import BatterCard
from apps.pitcher_card import PitcherCard


class TeamCard(tk.Toplevel):
    def __init__(self, selected_team=None):
        super().__init__()

        self.title(f"Team Card for {selected_team}")
        self.geometry("1920x1080")
        self.selected_team = selected_team

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
        self.batter_frame = DataFrameTableFrame(self.main_frame, batters, on_row_double_click=self.open_batter_card)
        self.batter_frame.grid(row=0, column=0, sticky="nsew")

        self.pitcher_frame = DataFrameTableFrame(self.main_frame, pitchers, on_row_double_click=self.open_pitcher_card)
        self.pitcher_frame.grid(row=0, column=1, sticky="nsew")

    def open_batter_card(self, row: pd.Series):
        try:
            card_id = int(row.get('CID'))
        except:
            return

        BatterCard(card_id, selected_team=self.selected_team)

    def open_pitcher_card(self, row: pd.Series):
        try:
            card_id = int(row.get('CID'))
        except:
            return

        PitcherCard(card_id, team_select=self.selected_team)