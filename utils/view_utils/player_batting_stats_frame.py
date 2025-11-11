import tkinter as tk
from utils.view_utils.stat_label import StatLabel
from utils.view_utils import program_fonts as fonts


class PlayerStatsFrameBatter(tk.Frame):
    def __init__(self, parent, title, stats):
        super().__init__(parent)

        stats_list = [
            ('PA: ', stats['ply_pa']),
            ('AVG: ', stats['ply_avg']),
            ('OBP: ', stats['ply_obp']),
            ('SLG: ', stats['ply_slg']),
            ('OPS: ', stats['ply_ops']),
            ('wOBA: ', stats['ply_woba']),
            ('HR: ', stats['ply_hr_rate']),
            ('K/600: ', stats['ply_k']),
            ('BB/600: ', stats['ply_bb']),
            ('SB/600: ', stats['ply_sb']),
            ('SB%: ', stats['ply_sb_pct']),
            ('WAR: ', stats['ply_war']),
        ]

        self.label = tk.Label(self, text=title, font=fonts.frame_title_font)
        self.label.grid(row=0, column=0, sticky='nsew')

        row = 1
        for text, value in stats_list:
            label = StatLabel(self, text, value)
            label.grid(row=row, column=0, pady=(0, 2), sticky='ew')
            row += 1
