import tkinter as tk
import pandas as pd

from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.stats_utils.generate_batter_slide_df import generate_batter_slide_df
from utils.view_utils.player_card_bat_ratings_frame import BatterRatingFrame
from utils.view_utils.player_card_defense_ratings_frame import PlayerCardDefenseRatingsFrame
from utils.view_utils.batter_profile_frame import BatterProfileFrame
from utils.view_utils.batter_slideshow_stats_frame import BatterSlideshowStatsFrame


class BatterSlideshowApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Batting Leaders')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        self.header_frame = Header(
            self,
            app_name="Batting Leaders"
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)

        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.rowconfigure(1, weight=0)
        self.main_frame.rowconfigure(2, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        self.rank_var = tk.IntVar(value=5)

        self.player_title = tk.Label(self.main_frame, text=f'Position Rank {self.rank_var.get()}')
        self.player_title.grid(row=0, column=0, sticky="nsew", columnspan=2)

        self.slide_df = generate_batter_slide_df()
        self.batter_df = self.slide_df.iloc[[4]]

        self.batting_ratings_frame = BatterRatingFrame(self.main_frame, self.batter_df)
        self.batting_ratings_frame.grid(row=1, column=0, sticky="nsew")

        self.defense_positions_frame = PlayerCardDefenseRatingsFrame(self.main_frame, self.batter_df)
        self.defense_positions_frame.grid(row=1, column=1, sticky="nsew")

        self.batter_profile_frame = BatterProfileFrame(self.main_frame, self.batter_df)
        self.batter_profile_frame.grid(row=1, column=2, sticky="nsew")

        self.batter_stats_frame = BatterSlideshowStatsFrame(self.main_frame, self.batter_df)
        self.batter_stats_frame.grid(row=2, column=0, sticky="nsew")

        self.previous_button = tk.Button(self.main_frame, text="PREVIOUS",
                                         command=self.previous_batter)
        self.previous_button.grid(row=3, column=0, sticky="nsew")

        self.next_button = tk.Button(self.main_frame, text="NEXT", command=self.next_batter)
        self.next_button.grid(row=3, column=2, sticky="nsew")

        self.update_batter(self.rank_var.get())

    def update_batter(self, rank):
        self.batter_df = self.slide_df.iloc[[rank - 1]]
        self.player_title.configure(text=f'Position Rank {self.rank_var.get()} {self.batter_df.iloc[0]['Title']}')
        self.batter_stats_frame.update_batter(self.batter_df)

    def next_batter(self):
        if self.rank_var.get() > 1:
            self.rank_var.set(self.rank_var.get() - 1)
            self.update_batter(self.rank_var.get())

    def previous_batter(self):
        if self.rank_var.get() < self.slide_df.size:
            self.rank_var.set(self.rank_var.get() + 1)
            self.update_batter(self.rank_var.get())






