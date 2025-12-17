import tkinter as tk
from tkinter import ttk
from utils.view_utils import program_fonts as fonts
from utils.stats_utils.get_player_batting_stats import get_player_batting_stats
from utils.view_utils.player_batting_stats_frame import PlayerStatsFrameBatter


class PlayerBattingStatsFrame(tk.Frame):
    def __init__(self, parent, card_id, team_select=None):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self, text='Player Stats', font=fonts.frame_title_font)
        self.label.grid(row=0, column=0, columnspan=3)

        player_stats_all = get_player_batting_stats(card_id)
        player_stats_recent = get_player_batting_stats(
            card_id=card_id, cutoff_days=7)
        player_stats_team = get_player_batting_stats(
            card_id=card_id, selected_team=team_select)

        self.player_stats_all_frame = PlayerStatsFrameBatter(
            self, title='All', stats=player_stats_all)
        self.player_stats_all_frame.grid(
            row=1, column=0, padx=(10, 10), pady=(3, 0))

        ttk.Separator(self, orient=tk.VERTICAL).grid(
            row=1, column=1, sticky='nsew')

        self.player_stats_recent_frame = PlayerStatsFrameBatter(
            self, title='Recent', stats=player_stats_recent
        )
        self.player_stats_recent_frame.grid(
            row=1, column=2, padx=(10, 10), pady=(3, 0)
        )
        ttk.Separator(self, orient=tk.VERTICAL).grid(
            row=1, column=3, sticky='nsew')

        self.player_stats_team_frame = PlayerStatsFrameBatter(
            self, title='Team', stats=player_stats_team)
        self.player_stats_team_frame.grid(
            row=1, column=4, padx=(10, 10), pady=(3, 0))
