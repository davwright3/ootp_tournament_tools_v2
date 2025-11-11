import tkinter as tk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.stat_label import StatLabel


class LeagueBattingStatsFrame(tk.Frame):
    def __init__(self, parent, stats):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)

        self.label = tk.Label(
            self,
            text='Batting',
            font=fonts.frame_title_font
        )
        self.label.grid(row=0, column=0, pady=(0, 10))

        stat_labels = [
            ('AVG: ', stats['lg_avg']),
            ('OBP: ', stats['lg_obp']),
            ('SLG: ', stats['lg_slg']),
            ('OPS: ', stats['lg_ops']),
            ('wOBA: ', stats['lg_woba']),
            ('HR: ', stats['lg_hr_rate']),
            ('SB/600: ', stats['lg_sb_rate']),
            ('SB%: ', stats['lg_sb_pct']),
        ]

        row = 1

        for text, value in stat_labels:
            lbl = StatLabel(self, text, value)
            lbl.grid(row=row, column=0, pady=(0, 2), sticky='ew')
            row += 1
