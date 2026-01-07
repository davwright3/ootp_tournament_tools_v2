import tkinter as tk
import pandas as pd
from utils.stats_utils.generate_pitcher_slide_df import (
    generate_pitcher_slide_df)
from utils.view_utils.player_card_pitcher_ratings_frame import (
    PlayerCardPitcherRatingsFrame)
from utils.view_utils.player_card_pitcher_profile_frame import (
    PlayerCardPitcherProfileFrame)
from utils.view_utils.player_card_individual_pitch_ratings_frame import (
    PlayerCardIndividualPitchRatingsFrame)
from utils.view_utils.pitcher_slideshow_stats_frame import (
    PitcherSlideshowStatsFrame)
from utils.view_utils.bats_throws_label import BatsThrowsLabel
from utils.view_utils.player_overall_rating_label import PlayerOverallRatingLabel
from utils.view_utils import program_fonts as fonts


class PitcherSlideFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.selected_rank = 10
        self.selected_player_df = pd.DataFrame()

        self.slide_df = generate_pitcher_slide_df()
        if self.selected_rank < len(self.slide_df):
            self.selected_player_df = self.slide_df.iloc[[self.selected_rank]]
        else:
            try:
                self.selected_player_df = self.slide_df.iloc[[len(self.slide_df) - 1]]
            except Exception as e:
                self.title_label = tk.Label(self,
                                            text='Not enough data to create slideshow',
                                            font=fonts.slideshow_header_font)
                self.title_label.grid(row=0, column=0, columnspan=3, sticky='nsew')
                return

        row = 0
        self.title_label = tk.Label(self, text="Pitcher Slide", font=fonts.slideshow_header_font)
        self.title_label.grid(column=0, row=row, sticky='nsew', columnspan=5)
        row += 1

        self.bats_label = BatsThrowsLabel(self, label_type='Bats', side_id=self.selected_player_df.iloc[0]['Bats'])
        self.bats_label.grid(column=0, row=row, sticky='nsew')

        self.overall_rating_label = PlayerOverallRatingLabel(self, value=self.selected_player_df.iloc[0]['Val'])
        self.overall_rating_label.grid(column=1, row=row, sticky='nsew')

        self.throws_label = BatsThrowsLabel(self, label_type='Throws', side_id=self.selected_player_df.iloc[0]['Throws'])
        self.throws_label.grid(column=2, row=row, sticky='nsew')
        row += 1

        self.ratings_frame = PlayerCardPitcherRatingsFrame(self, self.selected_player_df)
        self.ratings_frame.grid(row=row, column=0, sticky='nsew')

        self.pitcher_profile_frame = PlayerCardPitcherProfileFrame(self, self.selected_player_df)
        self.pitcher_profile_frame.grid(row=row, column=1, sticky='nsew')

        self.individual_pitches_frame = PlayerCardIndividualPitchRatingsFrame(self, self.selected_player_df)
        self.individual_pitches_frame.grid(row=row, column=2, sticky='nsew')
        row += 1

        self.stats_frame = PitcherSlideshowStatsFrame(self, self.selected_player_df, numquals=len(self.slide_df))
        self.stats_frame.grid(row=row, column=0, sticky='nsew', columnspan=3)
        row += 1

        self.all_pitchers_button = tk.Button(self, text='All', command=self.set_all_pitchers)
        self.all_pitchers_button.grid(row=row, column=0, sticky='nsew')

        self.starting_pitchers_button = tk.Button(self, text='SP', command=self.set_starting_pitchers)
        self.starting_pitchers_button.grid(row=row, column=1, sticky='nsew')

        self.relief_pitchers_button = tk.Button(self, text='RP', command=self.set_relief_pitchers)
        self.relief_pitchers_button.grid(row=row, column=2, sticky='nsew')
        row += 1

        self.previous_button = tk.Button(self, text='Previous', command=self.set_previous)
        self.previous_button.grid(row=row, column=0, sticky='nsew')

        self.next_button = tk.Button(self, text='Next', command=self.set_next)
        self.next_button.grid(row=row, column=2, sticky='nsew')

        self.update_slide(self.selected_rank)


    def update_slide(self, rank):
        self.selected_player_df = self.slide_df.iloc[[rank - 1]]
        card_name = self.selected_player_df.iloc[0]['Title']
        self.title_label.configure(text=card_name)
        self.bats_label.update_rating('Bats', self.selected_player_df.iloc[0]['Bats'])
        self.overall_rating_label.update_overall_rating_label(self.selected_player_df.iloc[0]['Val'])
        self.throws_label.update_rating('Throws', self.selected_player_df.iloc[0]['Throws'])
        self.ratings_frame.update_frame(self.selected_player_df)
        self.pitcher_profile_frame.update_frame(self.selected_player_df)
        self.individual_pitches_frame.update_frame(self.selected_player_df)
        self.stats_frame.update_frame(self.selected_player_df, num_quals=len(self.slide_df))

    def set_all_pitchers(self):
        self.slide_df = generate_pitcher_slide_df(pitcher_type=None)
        if len(self.slide_df) > 9:
            self.selected_rank = 10
        else:
            self.selected_rank = len(self.slide_df - 1)
        self.update_slide(self.selected_rank)
        return

    def set_starting_pitchers(self):
        self.slide_df = generate_pitcher_slide_df(pitcher_type='SP')
        if len(self.slide_df) > 9:
            self.selected_rank = 10
        else:
            self.selected_rank = len(self.slide_df - 1)
        self.update_slide(self.selected_rank)
        return

    def set_relief_pitchers(self):
        self.slide_df = generate_pitcher_slide_df(pitcher_type='RP')
        if len(self.slide_df) > 9:
            self.selected_rank = 10
        else:
            self.selected_rank = len(self.slide_df - 1)
        self.update_slide(self.selected_rank)
        return

    def set_next(self):
        if self.selected_rank > 1:
            self.selected_rank = self.selected_rank - 1
        self.update_slide(self.selected_rank)

    def set_previous(self):
        if self.selected_rank < (len(self.slide_df) -1):
            self.selected_rank = self.selected_rank + 1
        self.update_slide(self.selected_rank)
