import tkinter as tk
from utils.stats_utils.get_player_pitching_stats import (
    get_player_pitching_stats)
from utils.view_utils.stat_label import StatLabel


class PlayerPitchingStatsFrame(tk.Frame):
    def __init__(self, parent, label='', card_id=None, team_select=None, cutoff_days=None):
        super().__init__(parent)

        if team_select is None and cutoff_days is None:
            stats = get_player_pitching_stats(card_id)
        elif team_select is None:
            stats = get_player_pitching_stats(card_id, cutoff_days=cutoff_days)
        else:
            stats = get_player_pitching_stats(
                card_id=card_id, team_select=team_select)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(self, text=label)
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=2)

        stats_list = [
            ('IP: ', stats['ply_ip']),
            ('ERA: ', stats['ply_era']),
            ('FIP: ', stats['ply_fip']),
            ('K%: ', stats['ply_k_pct']),
            ('BB%: ', stats['ply_bb_pct']),
            ('K-BB: ', stats['ply_k-bb']),
            ('HR/600: ', stats['ply_hr_rate']),
            ('SV%: ', stats['ply_sv_pct']),
            ('SD/MD: ', stats['ply_sd_md']),
            ('IRS%: ', stats['ply_irs_pct']),
            ('IP/g: ', stats['ply_ipg']),
            ('GB%: ', stats['ply_gb_pct']),
            ('QS%: ', stats['ply_qs_pct']),
            ('WAR/600: ', stats['ply_war_rate']),
            ('oBABIP: ', stats['ply_babip']),
        ]

        row = 1
        for stat, value in stats_list:
            label = StatLabel(self, stat, value)
            label.grid(row=row, column=0, sticky='nsew')
            row += 1
