import tkinter as tk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.stat_label import StatLabel


class LeaguePitchingStatsFrame(tk.Frame):
    def __init__(self, parent, stats):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        self.label = tk.Label(
            self, text="Pitching", font=fonts.frame_title_font)
        self.label.grid(row=0, column=0)

        pitching_stats = [
            ('ERA: ', stats['lg_era']),
            ('GB%: ', stats['lg_gb_rate']),
            ('K%: ', stats['lg_so_rate']),
            ('BB%: ', stats['lg_bb_rate']),
            ('QS%: ', stats['lg_qs_pct']),
            ('IRS%: ', stats['lg_irs_pct']),
            ('SD/MD: ', stats['lg_sd_per_md']),
            ('FLD%: ', stats['lg_fld_pct']),
        ]

        row = 1
        for text, value in pitching_stats:
            label = StatLabel(self, text, value)
            label.grid(row=row, column=0, pady=(2, 0))
            row += 1
