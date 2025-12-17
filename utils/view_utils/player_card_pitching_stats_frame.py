import tkinter as tk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.player_pitching_stats_frame import (
    PlayerPitchingStatsFrame)


class PlayerCardPitchingStatsFrame(tk.Frame):
    def __init__(self, parent, card_id, team_select):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self, text="Player Pitching Stats", font=fonts.frame_title_font)
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=2)

        self.player_pitching_stats_all_frame = (
            PlayerPitchingStatsFrame(self, card_id=card_id))
        self.player_pitching_stats_all_frame.grid(row=1, column=0)

        self.player_pitching_stats_recent_frame = (
            PlayerPitchingStatsFrame(self, card_id=card_id, cutoff_days=7)
        )
        self.player_pitching_stats_recent_frame.grid(row=1, column=1)

        self.player_pitching_stats_team_frame = (
            PlayerPitchingStatsFrame(
                self, card_id=card_id, team_select=team_select))
        self.player_pitching_stats_team_frame.grid(row=1, column=2)
