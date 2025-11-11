import tkinter as tk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.league_batting_stats_frame import LeagueBattingStatsFrame
from utils.view_utils.league_pitching_stats_frame import (
    LeaguePitchingStatsFrame)
from utils.data_utils.league_stats_store import league_stats_store


class PlayerCardLeagueStatsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        lg_stats = league_stats_store.get_stats()

        self.label = tk.Label(
            self,
            text='League Stats',
            font=fonts.frame_title_font
        )
        self.label.grid(row=0, column=0, columnspan=3)

        self.batting_stats_frame = LeagueBattingStatsFrame(self, lg_stats)
        self.batting_stats_frame.grid(row=1, column=0, padx=(30, 0))

        self.pitching_stats_frame = LeaguePitchingStatsFrame(self, lg_stats)
        self.pitching_stats_frame.grid(row=1, column=1, padx=(30, 0))
