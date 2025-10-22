"""Batter card for displaying individual batter stats."""
import tkinter as tk
from utils.stats_utils.set_batter_card_data import set_batter_card_data
from utils.view_utils.player_card_bat_rattings_frame import BatterRattingFrame
from utils.view_utils.batter_profile_frame import BatterProfileFrame
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer

class BatterCard(tk.Toplevel):
    def __init__(self, card_id=None):
        super().__init__()

        self.title(f'Batter Card for {card_id}')
        self.geometry('1920x1080')

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        player_df = set_batter_card_data(card_id=int(card_id))

        self.header_frame = Header(self, app_name=f'Batter Card for {card_id}')
        self.header_frame.grid(row=0, column=0, sticky='nsew')

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky='nsew')

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky='nsew')

        # Individual frames
        self.batting_ratings_frame = BatterRattingFrame(self.main_frame, df=player_df)
        self.batting_ratings_frame.grid(row=0, column=0, sticky='nsew')

        self.batter_profile_frame = BatterProfileFrame(self.main_frame, df=player_df)
        self.batter_profile_frame.grid(row=0, column=1, sticky='nsew')