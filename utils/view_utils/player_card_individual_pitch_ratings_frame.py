import tkinter as tk
from tkinter import ttk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.color_rating_code_label import ColorRatingLabel


class PlayerCardIndividualPitchRatingsFrame(tk.Frame):
    def __init__(self, parent, player_df):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)

        self.label = tk.Label(
            self, text="Individual Pitch Ratings", font=fonts.frame_title_font)
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=6)

        ttk.Separator(
            self, orient='horizontal').grid(row=1, column=0, sticky='nsew')

        self.fastball_label = tk.Label(
            self, text="FB: ", font=fonts.basic_font)
        self.fastball_label.grid(row=2, column=0, sticky='nsew')

        self.fastball_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Fastball'])
        self.fastball_rating_label.grid(row=2, column=1, sticky='nsew')

        self.cutter_label = tk.Label(self, text="CT: ", font=fonts.basic_font)
        self.cutter_label.grid(row=3, column=0, sticky='nsew')

        self.cutter_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Cutter'])
        self.cutter_rating_label.grid(row=3, column=1, sticky='nsew')

        self.sinker_label = tk.Label(self, text="SI: ", font=fonts.basic_font)
        self.sinker_label.grid(row=4, column=0, sticky='nsew')

        self.sinker_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Sinker'])
        self.sinker_rating_label.grid(row=4, column=1, sticky='nsew')

        self.splitter_label = tk.Label(
            self, text="SP: ", font=fonts.basic_font)
        self.splitter_label.grid(row=5, column=0, sticky='nsew')

        self.splitter_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Splitter'])
        self.splitter_rating_label.grid(row=5, column=1, sticky='nsew')

        self.curveball_label = tk.Label(
            self, text="CB: ", font=fonts.basic_font)
        self.curveball_label.grid(row=2, column=2, sticky='nsew')

        self.curveball_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Curveball'])
        self.curveball_rating_label.grid(row=2, column=3, sticky='nsew')

        self.slider_label = tk.Label(self, text="SL: ", font=fonts.basic_font)
        self.slider_label.grid(row=3, column=2, sticky='nsew')

        self.slider_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Slider'])
        self.slider_rating_label.grid(row=3, column=3, sticky='nsew')

        self.forkball_label = tk.Label(
            self, text="FO: ", font=fonts.basic_font)
        self.forkball_label.grid(row=4, column=2, sticky='nsew')

        self.forkball_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Forkball'])
        self.forkball_rating_label.grid(row=4, column=3, sticky='nsew')

        self.screwball_label = tk.Label(
            self, text="SC: ", font=fonts.basic_font)
        self.screwball_label.grid(row=5, column=2, sticky='nsew')

        self.screwball_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Screwball'])
        self.screwball_rating_label.grid(row=5, column=3, sticky='nsew')

        self.changeup_label = tk.Label(
            self, text="CH: ", font=fonts.basic_font)
        self.changeup_label.grid(row=2, column=4, sticky='nsew')

        self.changeup_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=player_df.iloc[0]['Changeup'])
        self.changeup_rating_label.grid(row=2, column=5, sticky='nsew')

        self.circlechange_label = tk.Label(
            self, text="CC: ", font=fonts.basic_font)
        self.circlechange_label.grid(row=3, column=4, sticky='nsew')

        self.circlechange_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=player_df.iloc[0]['Circlechange'])
        self.circlechange_rating_label.grid(row=3, column=5, sticky='nsew')

        self.knucklecurve_label = tk.Label(
            self, text="KC: ", font=fonts.basic_font)
        self.knucklecurve_label.grid(row=4, column=4, sticky='nsew')

        self.knucklecurve_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=player_df.iloc[0]['Knucklecurve'])
        self.knucklecurve_rating_label.grid(row=4, column=5, sticky='nsew')

        self.knuckleball_label = tk.Label(
            self, text="KB: ", font=fonts.basic_font)
        self.knuckleball_label.grid(row=5, column=4, sticky='nsew')

        self.knuckleball_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=player_df.iloc[0]['Knuckleball'])
        self.knuckleball_rating_label.grid(row=5, column=5, sticky='nsew')

    def update_frame(self, player_df):
        self.fastball_rating_label.update_label(player_df.iloc[0]['Fastball'], font=fonts.basic_font)
        self.slider_rating_label.update_label(player_df.iloc[0]['Slider'], font=fonts.basic_font)
        self.curveball_rating_label.update_label(player_df.iloc[0]['Curveball'], font=fonts.basic_font)
        self.changeup_rating_label.update_label(player_df.iloc[0]['Changeup'], font=fonts.basic_font)
        self.cutter_rating_label.update_label(player_df.iloc[0]['Cutter'], font=fonts.basic_font)
        self.sinker_rating_label.update_label(player_df.iloc[0]['Sinker'], font=fonts.basic_font)
        self.splitter_rating_label.update_label(player_df.iloc[0]['Splitter'], font=fonts.basic_font)
        self.forkball_rating_label.update_label(player_df.iloc[0]['Forkball'], font=fonts.basic_font)
        self.screwball_rating_label.update_label(player_df.iloc[0]['Screwball'], font=fonts.basic_font)
        self.circlechange_rating_label.update_label(player_df.iloc[0]['Circlechange'], font=fonts.basic_font)
        self.knucklecurve_rating_label.update_label(player_df.iloc[0]['Knucklecurve'], font=fonts.basic_font)
        self.knuckleball_rating_label.update_label(player_df.iloc[0]['Knuckleball'], font=fonts.basic_font)
