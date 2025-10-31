"""App for displaying individual pitcher data."""
import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.player_card_pitcher_ratings_frame import PlayerCardPitcherRatingsFrame
from utils.view_utils.player_card_individual_pitch_ratings_frame import PlayerCardIndividualPitchRatingsFrame
from utils.view_utils.player_card_pitcher_profile_frame import PlayerCardPitcherProfileFrame
from utils.view_utils.player_card_pitching_stats_frame import PlayerCardPitchingStatsFrame
from utils.view_utils.player_card_league_stats_frame import PlayerCardLeagueStatsFrame
from utils.stats_utils.set_pitcher_card_data import set_pitcher_card_data

class PitcherCard(tk.Toplevel):
    def __init__(self, card_id=None, team_select=None):
        super().__init__()

        self.title(f'Pitcher Card for {card_id}')
        self.geometry('1920x1080')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        player_ratings_df = set_pitcher_card_data(card_id)

        self.columnconfigure(0, weight=1)

        self.header_frame = Header(self, app_name=f'Pitcher Card for {player_ratings_df.iloc[0]["//Card Title"]}')
        self.header_frame.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, columnspan=3, sticky='nsew')

        # Main frame setup
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.columnconfigure(3, weight=1)
        self.main_frame.columnconfigure(4, weight=1)
        self.main_frame.columnconfigure(5, weight=1)

        self.pitcher_ratings_frame = PlayerCardPitcherRatingsFrame(self.main_frame, player_ratings_df)
        self.pitcher_ratings_frame.grid(row=0, column=0, sticky='nsew')

        self.pitcher_profile_frame = PlayerCardPitcherProfileFrame(self.main_frame, player_ratings_df)
        self.pitcher_profile_frame.grid(row=0, column=1, sticky='nsew')

        self.individual_pitch_frame = PlayerCardIndividualPitchRatingsFrame(self.main_frame, player_ratings_df)
        self.individual_pitch_frame.grid(row=1, column=0, sticky='nsew', columnspan=2)

        self.player_stats_frame = PlayerCardPitchingStatsFrame(self.main_frame, card_id=card_id, team_select=team_select)
        self.player_stats_frame.grid(row=0, column=2, sticky='nsew', rowspan=2)

        self.league_stats_frame = PlayerCardLeagueStatsFrame(self.main_frame)
        self.league_stats_frame.grid(row=0, column=3, sticky='nsew', rowspan=2)


