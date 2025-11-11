"""Batter card for displaying individual batter stats."""
import tkinter as tk
from utils.stats_utils.set_batter_card_data import set_batter_card_data
from utils.view_utils.player_card_bat_ratings_frame import BatterRatingFrame
from utils.view_utils.baserunning_profile_frame import BaserunningProfileFrame
from utils.view_utils.player_card_batting_stats_frame import PlayerBattingStatsFrame
from utils.view_utils.batter_profile_frame import BatterProfileFrame
from utils.view_utils.player_card_league_stats_frame import PlayerCardLeagueStatsFrame
from utils.view_utils.player_card_defense_ratings_frame import PlayerCardDefenseRatingsFrame
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer

class BatterCard(tk.Toplevel):
    def __init__(self, card_id=None, selected_team=None):
        super().__init__()

        self.title(f'Batter Card for {card_id}')
        self.geometry('1920x1080')

        self.selected_team = selected_team

        self.columnconfigure(0, weight=1)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        player_df = set_batter_card_data(card_id=int(card_id))

        self.header_frame = Header(self, app_name=f'Batter Card for {player_df.iloc[0]["//Card Title"]}')
        self.header_frame.grid(row=0, column=0, sticky='nsew')

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky='nsew')

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky='nsew')

        # Individual frames
        self.batting_ratings_frame = BatterRatingFrame(self.main_frame, df=player_df)
        self.batting_ratings_frame.grid(row=0, column=0, sticky='nsew')

        self.baserunning_frame = BaserunningProfileFrame(self.main_frame, df=player_df)
        self.baserunning_frame.grid(row=0, column=1, sticky='nsew')

        self.batter_profile_frame = BatterProfileFrame(self.main_frame, df=player_df)
        self.batter_profile_frame.grid(row=0, column=2, sticky='nsew')

        self.defense_ratings_frame = PlayerCardDefenseRatingsFrame(self.main_frame, df=player_df)
        self.defense_ratings_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.player_batting_stats_frame = PlayerBattingStatsFrame(self.main_frame, card_id=int(card_id), team_select=self.selected_team)
        self.player_batting_stats_frame.grid(row=0, column=3, rowspan=2, sticky='nsew')

        self.league_stats_frame = PlayerCardLeagueStatsFrame(self.main_frame)
        self.league_stats_frame.grid(row=0, column=4, rowspan=2, sticky='nsew')
