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
from utils.view_utils.table_formatters import fmt_leading_dot
from utils.view_utils.min_max_rating_frame import MinMaxFrame
from utils.view_utils.scrollable_frame import ScrollableFrame


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
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

        # Set up the options frame
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(row=0, column=1, sticky='nsew')

        self.options_frame.columnconfigure(0, weight=1)
        self.options_frame.columnconfigure(1, weight=1)
        self.options_frame.columnconfigure(2, weight=1)
        self.options_frame.rowconfigure(0, weight=0)
        self.options_frame.rowconfigure(1, weight=1)

        self.options_button_frame = ttk.Frame(self.options_frame)
        self.options_button_frame.grid(row=0, column=0, sticky='nsew')
        self.options_button_frame.columnconfigure(0, weight=1)
        self.options_button_frame.columnconfigure(1, weight=0)
        self.options_button_frame.columnconfigure(2, weight=1)

        self.load_data_button = tk.Button(
            self.options_button_frame,
            text='Reload',
            command=self.reload_data,
            width=5,
            height=1,
        )
        self.load_data_button.grid(row=0, column=1, ipadx=5, ipady=5, sticky='nsew')

        # Frame for the various user options to select
        self.options_select_frame = ScrollableFrame(
            self.options_button_frame,
            yscroll=True,
            xscroll=False,
        )
        self.options_select_frame.grid(row=1, column=0, columnspan=3, sticky='nsew')

        self.min_max_frame = MinMaxFrame(self.options_select_frame)
        self.min_max_frame.grid(row=0, column=0, sticky='nsew')

        # Set up initial dataframe for the table
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
        self.dataframe_frame.grid(row=0, column=0, sticky='nsew')

    def reload_data(self):
        """Reload the data to the dataframe."""
        stats_df = calc_basic_batting_stats_df(stat_list=['PA', 'OBP', 'wOBA'])
        self.dataframe_frame.set_dataframe(stats_df)

