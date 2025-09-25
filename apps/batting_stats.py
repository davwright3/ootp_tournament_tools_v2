"""
Main app for displaying batting stats for all players.

Opens a tkinter TopLevel app, and gets data from the
loaded data store to display in a custom frame for
displaying DataFrames.
"""
import tkinter as tk
from tkinter import ttk

from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.stats_utils.calc_basic_batting_stats_df import calc_basic_batting_stats_df
from utils.view_utils.batter_dataframe_table_frame import BatterDataFrameTableFrame
from utils.view_utils.batting_table_formatters import fmt_leading_dot


class BattingStatsApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Batting Stats')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.header_frame = Header(self, app_name='Batting Stats App')
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky='nsew')

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

        stats_df = calc_basic_batting_stats_df()

        fmt = {
            'AVG': fmt_leading_dot(3, '.000'),
            'OBP': fmt_leading_dot(3, '.000'),
            'SLG': fmt_leading_dot(3, '.000'),
            'OPS': fmt_leading_dot(3, '.000'),
            'wOBA': fmt_leading_dot(3, '.000'),
            'HRrate': fmt_leading_dot(1, '.0'),
            'Krate': fmt_leading_dot(1, '.0'),
            'BBrate': fmt_leading_dot(1, '.0'),
            'SBrate': fmt_leading_dot(1, '.0'),
            'SBpct': fmt_leading_dot(3, '.000'),
            'WARrate': fmt_leading_dot(1, '.0')
        }

        self.dataframe_frame = BatterDataFrameTableFrame(self.main_frame, df=stats_df, formatters=fmt)
        self.dataframe_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

