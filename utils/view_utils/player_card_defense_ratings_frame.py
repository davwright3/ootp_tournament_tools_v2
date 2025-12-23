import tkinter as tk
from tkinter import ttk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.defense_ratings_frame import DefenseRatingsFrame
from utils.view_utils.eligible_defense_positions_frame import (
    EligibleDefensePositionsFrame)


class PlayerCardDefenseRatingsFrame(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)

        self.label = tk.Label(
            self, text='Defense Ratings', font=fonts.frame_title_font)
        self.label.grid(row=0, column=0, columnspan=3, sticky='ew')

        self.ratings_frame = DefenseRatingsFrame(self, df)
        self.ratings_frame.grid(row=1, column=0, sticky='nsew')

        ttk.Separator(
            self, orient='vertical').grid(row=1, column=1, sticky='nsew')

        self.eligibility_frame = EligibleDefensePositionsFrame(self, df)
        self.eligibility_frame.grid(row=1, column=2, sticky='nsew')

    def update_frame(self, df):
        self.ratings_frame.update_frame(df)
        self.eligibility_frame.update_frame(df)
